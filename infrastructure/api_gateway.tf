resource "aws_api_gateway_rest_api" "rest_api" {
  name = "business_rest_api"
}

resource "aws_api_gateway_deployment" "deploy_api" {
  rest_api_id = aws_api_gateway_rest_api.rest_api.id

  triggers = {
    redeployment = sha1(jsonencode(aws_api_gateway_rest_api.rest_api.body))
  }

  lifecycle {
    create_before_destroy = true
  }

  depends_on = [ 
    aws_api_gateway_integration.integration_api_users_post, 
    aws_api_gateway_integration.integration_api_user_get, 
    aws_api_gateway_integration.integration_api_user_put, 
    aws_api_gateway_integration.integration_api_user_delete,
    aws_api_gateway_method.put_user,
    aws_api_gateway_method.get_user,
    aws_api_gateway_method.post_users,
    aws_api_gateway_method.delete_user,
    aws_api_gateway_integration.integration_api_clients_post,
    aws_api_gateway_integration.integration_api_client_get,
    aws_api_gateway_integration.integration_api_client_put,
    aws_api_gateway_integration.integration_api_client_delete,
    aws_api_gateway_method.post_clients,
    aws_api_gateway_method.get_client,
    aws_api_gateway_method.put_client,
    aws_api_gateway_method.delete_client,
    aws_api_gateway_integration.integration_api_sales_post,
    aws_api_gateway_integration.integration_api_sale_get,
    aws_api_gateway_integration.integration_api_sale_put,
    aws_api_gateway_integration.integration_api_sale_delete,
    aws_api_gateway_method.post_sales,
    aws_api_gateway_method.get_sale,
    aws_api_gateway_method.put_sale,
    aws_api_gateway_method.delete_sale,
  ]
}

resource "aws_api_gateway_stage" "name" {
  deployment_id = aws_api_gateway_deployment.deploy_api.id
  rest_api_id = aws_api_gateway_rest_api.rest_api.id
  stage_name = "dev"
}
