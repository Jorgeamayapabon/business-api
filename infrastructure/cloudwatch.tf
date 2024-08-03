resource "aws_cloudwatch_log_group" "log_group" {
  name = "/aws/lambda/${var.lambda_function_name}"
  retention_in_days = 1
}

resource "aws_cloudwatch_log_group" "log_group_sales_processor" {
  name = "/aws/lambda/${var.lambda_sales_processor_name}"
  retention_in_days = 1
}

resource "aws_cloudwatch_log_group" "log_group_event_processor" {
  name = "/aws/lambda/${var.lambda_event_processor_name}"
  retention_in_days = 1
}