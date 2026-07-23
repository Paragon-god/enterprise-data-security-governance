# Northstar Retail model governance reference
#
# This sanitised script is based on the implemented prototype.
# Supply a lawful retail CSV source before execution.

set.seed(304)

sales_data <- read.csv(
  file = "data/retail_transactions.csv",
  stringsAsFactors = FALSE,
  check.names = TRUE
)

model_data <- data.frame(
  profit = as.numeric(sales_data$Profit),
  sales = as.numeric(sales_data$Sales),
  quantity = as.numeric(sales_data$Quantity),
  discount = as.numeric(sales_data$Discount),
  category = as.factor(sales_data$Category),
  segment = as.factor(sales_data$Segment),
  region = as.factor(sales_data$Region)
)

model_data <- model_data[complete.cases(model_data), ]

train_index <- sample(
  seq_len(nrow(model_data)),
  size = floor(0.80 * nrow(model_data))
)

train_data <- model_data[train_index, ]
test_data <- model_data[-train_index, ]

profit_model <- lm(
  profit ~ sales + quantity + discount + category + segment + region,
  data = train_data
)

predictions <- predict(profit_model, newdata = test_data)
actual <- test_data$profit

mae <- mean(abs(actual - predictions))
rmse <- sqrt(mean((actual - predictions) ^ 2))
r_squared <- 1 - sum((actual - predictions) ^ 2) /
  sum((actual - mean(actual)) ^ 2)

metrics <- data.frame(
  metric = c("MAE", "RMSE", "Test R Squared"),
  value = c(mae, rmse, r_squared)
)

print(summary(profit_model))
print(metrics)

write.csv(
  data.frame(actual_profit = actual, predicted_profit = predictions),
  file = "runtime_outputs/profit_model_predictions.csv",
  row.names = FALSE
)

write.csv(
  metrics,
  file = "runtime_outputs/model_metrics.csv",
  row.names = FALSE
)
