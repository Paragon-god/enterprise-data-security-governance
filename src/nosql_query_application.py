"""Sanitised MongoDB query application reference.

Set MONGODB_URI in the execution environment. Never commit the URI or
credential values.
"""

from __future__ import annotations

import os
from typing import Any

import certifi
import gradio as gr
import pandas as pd
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.server_api import ServerApi


ALLOWED_RECORD_TYPES = {
    "All Records": None,
    "Category Performance": "category_performance",
    "Regional Performance": "regional_performance",
    "Top Products": "top_product",
}


def get_collection() -> Collection:
    uri = os.getenv("MONGODB_URI")

    if not uri:
        raise RuntimeError("MONGODB_URI is not configured.")

    client = MongoClient(
        uri,
        server_api=ServerApi("1"),
        tlsCAFile=certifi.where(),
    )
    client.admin.command("ping")
    return client["northstar_retail"]["analytics_results"]


def query_analytics(
    collection: Collection,
    selected_type: str,
    minimum_sales: float | None,
) -> tuple[pd.DataFrame, str]:
    record_type = ALLOWED_RECORD_TYPES.get(selected_type)

    if selected_type not in ALLOWED_RECORD_TYPES:
        raise ValueError("Record type is not permitted.")

    query: dict[str, Any] = {}

    if record_type:
        query["record_type"] = record_type

    threshold = float(minimum_sales or 0)

    if threshold < 0:
        raise ValueError("Minimum sales cannot be negative.")

    if threshold > 0:
        query["total_sales"] = {"$gte": threshold}

    documents = list(
        collection.find(
            query,
            {
                "_id": 0,
                "source": 0,
                "inserted_at": 0,
            },
        ).sort("total_sales", -1)
    )

    if not documents:
        return (
            pd.DataFrame({"Result": ["No records matched the filters."]}),
            "0 records returned.",
        )

    frame = pd.DataFrame(documents)
    preferred = [
        "record_type",
        "name",
        "total_sales",
        "total_profit",
        "total_quantity",
        "units_sold",
        "unique_orders",
    ]
    columns = [column for column in preferred if column in frame.columns]

    return frame[columns], f"{len(frame)} records returned from MongoDB."


def build_application() -> gr.Blocks:
    collection = get_collection()

    def run_query(
        selected_type: str,
        minimum_sales: float | None,
    ) -> tuple[pd.DataFrame, str]:
        return query_analytics(collection, selected_type, minimum_sales)

    with gr.Blocks(
        title="Northstar Retail Data Governance Query Application"
    ) as application:
        gr.Markdown("# Northstar Retail Data Governance Query Application")
        gr.Markdown(
            "Query approved analytical summaries stored in MongoDB."
        )

        with gr.Row():
            record_type = gr.Dropdown(
                choices=list(ALLOWED_RECORD_TYPES),
                value="All Records",
                label="Record Type",
            )
            minimum_sales = gr.Number(
                value=0,
                label="Minimum Total Sales",
                precision=2,
            )

        query_button = gr.Button("Query MongoDB")
        status = gr.Markdown()
        results = gr.Dataframe(
            label="Approved Analytical Results",
            interactive=False,
        )

        query_button.click(
            fn=run_query,
            inputs=[record_type, minimum_sales],
            outputs=[results, status],
        )

    return application


if __name__ == "__main__":
    build_application().launch()
