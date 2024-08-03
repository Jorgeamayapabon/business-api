### METHODS TO USERS
# Method POST /users
resource "aws_api_gateway_method" "post_users" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  resource_id = aws_api_gateway_resource.users_resource.id
  http_method = "POST"
  authorization = "NONE"
}

# Method GET /users/{user_id}
resource "aws_api_gateway_method" "get_user" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  resource_id = aws_api_gateway_resource.user_id_resource.id
  http_method = "GET"
  authorization = "NONE"
}

# Method PUT /users/{user_id}
resource "aws_api_gateway_method" "put_user" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  resource_id = aws_api_gateway_resource.user_id_resource.id
  http_method = "PUT"
  authorization = "NONE"
}

# Method DELETE /users/{user_id}
resource "aws_api_gateway_method" "delete_user" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  resource_id = aws_api_gateway_resource.user_id_resource.id
  http_method = "DELETE"
  authorization = "NONE"
}

### METHODS TO CLIENTS
# Method POST /clients
resource "aws_api_gateway_method" "post_clients" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  resource_id = aws_api_gateway_resource.clients_resource.id
  http_method = "POST"
  authorization = "NONE"
}

# Method GET /clients/{client_id}
resource "aws_api_gateway_method" "get_client" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  resource_id = aws_api_gateway_resource.client_id_resource.id
  http_method = "GET"
  authorization = "NONE"
}

# Method PUT /clients/{client_id}
resource "aws_api_gateway_method" "put_client" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  resource_id = aws_api_gateway_resource.client_id_resource.id
  http_method = "PUT"
  authorization = "NONE"
}

# Method DELETE /clients/{client_id}
resource "aws_api_gateway_method" "delete_client" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  resource_id = aws_api_gateway_resource.client_id_resource.id
  http_method = "DELETE"
  authorization = "NONE"
}

### METHODS TO SALES
# Method POST /sales
resource "aws_api_gateway_method" "post_sales" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  resource_id = aws_api_gateway_resource.sales_resource.id
  http_method = "POST"
  authorization = "NONE"
}

# Method GET /sales/{sale_id}
resource "aws_api_gateway_method" "get_sale" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  resource_id = aws_api_gateway_resource.sale_id_resource.id
  http_method = "GET"
  authorization = "NONE"
}

# Method PUT /sales/{sale_id}
resource "aws_api_gateway_method" "put_sale" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  resource_id = aws_api_gateway_resource.sale_id_resource.id
  http_method = "PUT"
  authorization = "NONE"
}

# Method DELETE /sales/{sale_id}
resource "aws_api_gateway_method" "delete_sale" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  resource_id = aws_api_gateway_resource.sale_id_resource.id
  http_method = "DELETE"
  authorization = "NONE"
}