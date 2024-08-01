resource "aws_lambda_function" "lambda" {
    function_name = var.lambda_function_name
    handler = "lambda_function.lambda_handler"
    runtime = "python3.10"
    role = aws_iam_role.lambda_role.arn
    filename = "business-api.zip"
    depends_on = [ 
        aws_iam_role_policy_attachment.lambda_logs,
        aws_cloudwatch_log_group.log_group
     ]
}
