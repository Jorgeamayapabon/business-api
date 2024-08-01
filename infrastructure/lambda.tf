resource "aws_lambda_function" "lambda_api" {
  function_name = var.lambda_function_name
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.10"
  role          = aws_iam_role.lambda_api_role.arn
  filename      = "business-api.zip"
  depends_on = [
    aws_iam_role_policy_attachment.lambda_attachment,
    aws_cloudwatch_log_group.log_group
  ]
}

resource "aws_lambda_permission" "lambda_permission_api" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_api.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.rest_api.execution_arn}/*"
}
