resource "aws_api_gateway_rest_api" "rest_api" {
  name = "business_rest_api"
}

resource "aws_api_gateway_resource" "users_resource" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  parent_id = aws_api_gateway_rest_api.rest_api.root_resource_id
  path_part = var.users_path
}

resource "aws_api_gateway_resource" "user_id_resource" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  parent_id = aws_api_gateway_rest_api.rest_api.root_resource_id
  path_part = var.user_id_path
}

resource "aws_api_gateway_method" "post_users" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  resource_id = aws_api_gateway_resource.users_resource.id
  http_method = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "get_user" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  resource_id = aws_api_gateway_resource.user_id_resource.id
  http_method = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "put_user" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  resource_id = aws_api_gateway_resource.user_id_resource.id
  http_method = "PUT"
  authorization = "NONE"
}

resource "aws_api_gateway_method" "delete_user" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  resource_id = aws_api_gateway_resource.user_id_resource.id
  http_method = "DELETE"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "integration_api" {
    rest_api_id = aws_api_gateway_rest_api.rest_api.id
    resource_id = aws_api_gateway_resource.users_resource.id
    http_method = aws_api_gateway_method.post_users.http_method
    integration_http_method = "POST"
    type = "AWS_PROXY"
    uri = aws_lambda_function.lambda.invoke_arn
}

resource "aws_api_gateway_integration" "integration_api_get" {
    rest_api_id = aws_api_gateway_rest_api.rest_api.id
    resource_id = aws_api_gateway_resource.user_id_resource.id
    http_method = aws_api_gateway_method.get_user.http_method
    integration_http_method = "GET"
    type = "AWS_PROXY"
    uri = aws_lambda_function.lambda.invoke_arn
}

resource "aws_api_gateway_integration" "integration_api_put" {
    rest_api_id = aws_api_gateway_rest_api.rest_api.id
    resource_id = aws_api_gateway_resource.user_id_resource.id
    http_method = aws_api_gateway_method.put_user.http_method
    integration_http_method = "PUT"
    type = "AWS_PROXY"
    uri = aws_lambda_function.lambda.invoke_arn
}

resource "aws_api_gateway_integration" "integration_api_delete" {
    rest_api_id = aws_api_gateway_rest_api.rest_api.id
    resource_id = aws_api_gateway_resource.user_id_resource.id
    http_method = aws_api_gateway_method.delete_user.http_method
    integration_http_method = "DELETE"
    type = "AWS_PROXY"
    uri = aws_lambda_function.lambda.invoke_arn
}

resource "aws_lambda_permission" "lambda_permission" {
  statement_id = "AllowExecutionFromAPIGateway"
    action = "lambda:InvokeFunction"
    function_name = aws_lambda_function.lambda.function_name
    principal = "apigateway.amazonaws.com"
    source_arn = "${aws_api_gateway_rest_api.rest_api.execution_arn}/*"
}
