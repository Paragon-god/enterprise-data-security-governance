"""Reference controls for governed Spark ingestion.

This script is a sanitised portfolio reference based on the implemented
prototype. Supply a lawful CSV source and an approved output location.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import DoubleType, IntegerType


REQUIRED_COLUMNS = {
    "order_date",
    "ship_date",
    "sales",
    "quantity",
    "discount",
    "profit",
}


@dataclass(frozen=True)
class ValidationResult:
    source_count: int
    stored_count: int
    missing_required_columns: tuple[str, ...]
    null_counts: dict[str, int]


def normalise_column_name(name: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "_", name.strip())
    return value.strip("_").lower()


def load_controlled_csv(spark: SparkSession, source_path: str) -> DataFrame:
    frame = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .option("quote", '"')
        .option("escape", '"')
        .option("multiLine", True)
        .csv(source_path)
    )

    return frame.toDF(*[normalise_column_name(column) for column in frame.columns])


def convert_critical_fields(frame: DataFrame) -> DataFrame:
    return (
        frame
        .withColumn("order_date", F.to_date("order_date", "M/d/yyyy"))
        .withColumn("ship_date", F.to_date("ship_date", "M/d/yyyy"))
        .withColumn("sales", F.col("sales").cast(DoubleType()))
        .withColumn("quantity", F.col("quantity").cast(IntegerType()))
        .withColumn("discount", F.col("discount").cast(DoubleType()))
        .withColumn("profit", F.col("profit").cast(DoubleType()))
    )


def validate_frame(frame: DataFrame) -> tuple[tuple[str, ...], dict[str, int]]:
    missing = tuple(sorted(REQUIRED_COLUMNS.difference(frame.columns)))

    if missing:
        return missing, {}

    row = frame.select(
        *[
            F.sum(F.col(column).isNull().cast("int")).alias(column)
            for column in sorted(REQUIRED_COLUMNS)
        ]
    ).first()

    return missing, {column: int(row[column]) for column in sorted(REQUIRED_COLUMNS)}


def write_and_reconcile(
    frame: DataFrame,
    output_path: str,
) -> ValidationResult:
    missing, null_counts = validate_frame(frame)

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    if any(null_counts.values()):
        raise ValueError(f"Critical field validation failed: {null_counts}")

    source_count = frame.count()
    frame.write.mode("overwrite").parquet(output_path)

    spark = frame.sparkSession
    stored_count = spark.read.parquet(output_path).count()

    if source_count != stored_count:
        raise ValueError(
            f"Record count mismatch. Source: {source_count}. Stored: {stored_count}."
        )

    return ValidationResult(
        source_count=source_count,
        stored_count=stored_count,
        missing_required_columns=missing,
        null_counts=null_counts,
    )


def main() -> None:
    spark = SparkSession.builder.appName(
        "NorthstarRetailDataQualityControls"
    ).getOrCreate()

    source_path = str(Path("data") / "retail_transactions.csv")
    output_path = str(Path("runtime_outputs") / "cleaned_sales_parquet")

    raw = load_controlled_csv(spark, source_path)
    cleaned = convert_critical_fields(raw)
    result = write_and_reconcile(cleaned, output_path)

    print(result)
    spark.stop()


if __name__ == "__main__":
    main()
