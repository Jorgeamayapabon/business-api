# Resource /users
resource "aws_api_gateway_resource" "users_resource" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  parent_id = aws_api_gateway_rest_api.rest_api.root_resource_id
  path_part = var.users_path
}

# Resource /users/{user_id}
resource "aws_api_gateway_resource" "user_id_resource" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  parent_id = aws_api_gateway_resource.users_resource.id
  path_part = var.user_id_path
}

# Resource /clients
resource "aws_api_gateway_resource" "clients_resource" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  parent_id = aws_api_gateway_rest_api.rest_api.root_resource_id
  path_part = var.clients_path
}

# Resource /clients/{client_id}
resource "aws_api_gateway_resource" "client_id_resource" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  parent_id = aws_api_gateway_resource.clients_resource.id
  path_part = var.client_id_path
}

# Resource /sales
resource "aws_api_gateway_resource" "sales_resource" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  parent_id = aws_api_gateway_rest_api.rest_api.root_resource_id
  path_part = var.sales_path
}

# Resource /sales/{sale_id}
resource "aws_api_gateway_resource" "sale_id_resource" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  parent_id = aws_api_gateway_resource.sales_resource.id
  path_part = var.sale_id_path
}
