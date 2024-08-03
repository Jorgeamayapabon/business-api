resource "aws_cloudwatch_event_rule" "dynamodb_update_rule" {
  name        = "dynamodb_update_rule"
  description = "Rule for DynamoDB update event"
  event_pattern = jsonencode({
    source      = ["business-api"],
  })
}

resource "aws_cloudwatch_event_target" "dynamodb_update_target" {
  rule      = aws_cloudwatch_event_rule.dynamodb_update_rule.name
  target_id = "dynamodb_update_target"
  arn       = aws_lambda_function.lambda_event_processor.arn
}
