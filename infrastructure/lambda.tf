### Lambda function for API
# Lambda function for API
resource "aws_lambda_function" "lambda_api" {
  function_name = var.lambda_function_name
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.10"
  role          = aws_iam_role.lambda_api_role.arn
  filename      = "business-api.zip"
  layers = [ aws_lambda_layer_version.business_api_layer.arn ]
  timeout = 120

  depends_on = [
    aws_iam_role_policy_attachment.lambda_attachment,
    aws_cloudwatch_log_group.log_group
  ]

  environment {
    variables = {
      table_user = var.table_user_name,
      table_client = var.table_client_name,
      table_sale = var.table_sale_name,
      queue_sale_processor = var.queue_sale_processor_name
      region = var.region
    }
  }
}

# Lambda layer for API
resource "aws_lambda_layer_version" "business_api_layer" {
  layer_name = "business-api-layer"
  filename   = "business-api-layer.zip"
  compatible_runtimes = ["python3.10"]
  compatible_architectures = [ "x86_64" ]
}

# Lambda permission for API
resource "aws_lambda_permission" "lambda_permission_api" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_api.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.rest_api.execution_arn}/*"
}

### Lambda function for processing sales
# Lambda function for processing sales
resource "aws_lambda_function" "lambda_sales_processor" {
  function_name = var.lambda_sales_processor_name
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.10"
  role          = aws_iam_role.lambda_sales_processor_role.arn
  filename      = "sales-processor.zip"
  layers = [ aws_lambda_layer_version.business_api_layer.arn ]
  timeout = 50

  depends_on = [
    aws_iam_role_policy_attachment.lambda_sales_processor_attachment,
    aws_cloudwatch_log_group.log_group_sales_processor
  ]

  environment {
    variables = {
      table_user = var.table_user_name,
      table_client = var.table_client_name,
      table_sale = var.table_sale_name
      queue_sale_processor = var.queue_sale_processor_name
      region = var.region
      sns_topic_arn = aws_sns_topic.notification.arn
    }
  }
}

# Lambda permission for processing sales
resource "aws_lambda_permission" "permission_execution_sqs" {
  statement_id  = "AllowExecutionFromSQS"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_sales_processor.function_name
  principal     = "sqs.amazonaws.com"
  source_arn    = aws_sqs_queue.queue_sale_processor.arn
}

resource "aws_lambda_event_source_mapping" "trigger_sales_processor" {
  event_source_arn = aws_sqs_queue.queue_sale_processor.arn
  function_name    = aws_lambda_function.lambda_sales_processor.function_name
  batch_size       = 1
}

# Lambda permission for EventBridge
resource "aws_lambda_permission" "allow_eventbridge" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_sales_processor.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.dynamodb_update_rule.arn
}
