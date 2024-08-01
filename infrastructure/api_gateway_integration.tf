### INTEGRATIONS TO USERS
resource "aws_api_gateway_integration" "integration_api_users_post" {
    rest_api_id = aws_api_gateway_rest_api.rest_api.id
    resource_id = aws_api_gateway_resource.users_resource.id
    http_method = aws_api_gateway_method.post_users.http_method
    integration_http_method = "POST"
    type = "AWS_PROXY"
    uri = aws_lambda_function.lambda.invoke_arn
}

resource "aws_api_gateway_integration" "integration_api_user_get" {
    rest_api_id = aws_api_gateway_rest_api.rest_api.id
    resource_id = aws_api_gateway_resource.user_id_resource.id
    http_method = aws_api_gateway_method.get_user.http_method
    integration_http_method = "GET"
    type = "AWS_PROXY"
    uri = aws_lambda_function.lambda.invoke_arn
}

resource "aws_api_gateway_integration" "integration_api_user_put" {
    rest_api_id = aws_api_gateway_rest_api.rest_api.id
    resource_id = aws_api_gateway_resource.user_id_resource.id
    http_method = aws_api_gateway_method.put_user.http_method
    integration_http_method = "PUT"
    type = "AWS_PROXY"
    uri = aws_lambda_function.lambda.invoke_arn
}

resource "aws_api_gateway_integration" "integration_api_user_delete" {
    rest_api_id = aws_api_gateway_rest_api.rest_api.id
    resource_id = aws_api_gateway_resource.user_id_resource.id
    http_method = aws_api_gateway_method.delete_user.http_method
    integration_http_method = "DELETE"
    type = "AWS_PROXY"
    uri = aws_lambda_function.lambda.invoke_arn
}

### INTEGRATIONS TO CLIENTS
resource "aws_api_gateway_integration" "integration_api_clients_post" {
    rest_api_id = aws_api_gateway_rest_api.rest_api.id
    resource_id = aws_api_gateway_resource.clients_resource.id
    http_method = aws_api_gateway_method.post_clients.http_method
    integration_http_method = "POST"
    type = "AWS_PROXY"
    uri = aws_lambda_function.lambda.invoke_arn
}

resource "aws_api_gateway_integration" "integration_api_client_get" {
    rest_api_id = aws_api_gateway_rest_api.rest_api.id
    resource_id = aws_api_gateway_resource.client_id_resource.id
    http_method = aws_api_gateway_method.get_client.http_method
    integration_http_method = "GET"
    type = "AWS_PROXY"
    uri = aws_lambda_function.lambda.invoke_arn
}

resource "aws_api_gateway_integration" "integration_api_client_put" {
    rest_api_id = aws_api_gateway_rest_api.rest_api.id
    resource_id = aws_api_gateway_resource.client_id_resource.id
    http_method = aws_api_gateway_method.put_client.http_method
    integration_http_method = "PUT"
    type = "AWS_PROXY"
    uri = aws_lambda_function.lambda.invoke_arn
}

resource "aws_api_gateway_integration" "integration_api_client_delete" {
    rest_api_id = aws_api_gateway_rest_api.rest_api.id
    resource_id = aws_api_gateway_resource.client_id_resource.id
    http_method = aws_api_gateway_method.delete_client.http_method
    integration_http_method = "DELETE"
    type = "AWS_PROXY"
    uri = aws_lambda_function.lambda.invoke_arn
}

### INTEGRATIONS TO CLIENTS
resource "aws_api_gateway_integration" "integration_api_sales_post" {
    rest_api_id = aws_api_gateway_rest_api.rest_api.id
    resource_id = aws_api_gateway_resource.sales_resource.id
    http_method = aws_api_gateway_method.post_sales.http_method
    integration_http_method = "POST"
    type = "AWS_PROXY"
    uri = aws_lambda_function.lambda.invoke_arn
}

resource "aws_api_gateway_integration" "integration_api_sale_get" {
    rest_api_id = aws_api_gateway_rest_api.rest_api.id
    resource_id = aws_api_gateway_resource.sale_id_resource.id
    http_method = aws_api_gateway_method.get_sale.http_method
    integration_http_method = "GET"
    type = "AWS_PROXY"
    uri = aws_lambda_function.lambda.invoke_arn
}

resource "aws_api_gateway_integration" "integration_api_sale_put" {
    rest_api_id = aws_api_gateway_rest_api.rest_api.id
    resource_id = aws_api_gateway_resource.sale_id_resource.id
    http_method = aws_api_gateway_method.put_sale.http_method
    integration_http_method = "PUT"
    type = "AWS_PROXY"
    uri = aws_lambda_function.lambda.invoke_arn
}

resource "aws_api_gateway_integration" "integration_api_sale_delete" {
    rest_api_id = aws_api_gateway_rest_api.rest_api.id
    resource_id = aws_api_gateway_resource.sale_id_resource.id
    http_method = aws_api_gateway_method.delete_sale.http_method
    integration_http_method = "DELETE"
    type = "AWS_PROXY"
    uri = aws_lambda_function.lambda.invoke_arn
}
