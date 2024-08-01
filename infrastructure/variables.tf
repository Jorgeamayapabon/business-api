variable "lambda_function_name" {
    description = "name of the lambda function"
    type = string
    default = "business_api"
}

variable "users_path" {
    description = "path for the users resource"
    type = string
    default = "users"
}

variable "user_id_path" {
    description = "path for the user id resource"
    type = string
    default = "{user_id}"
}

variable "clients_path" {
    description = "path for the clients resource"
    type = string
    default = "clients"
  
}

variable "client_id_path" {
    description = "path for the client id resource"
    type = string
    default = "{client_id}"
}

variable "sales_path" {
    description = "path for the sales resource"
    type = string
    default = "sales"
}

variable "sale_id_path" {
    description = "path for the sale id resource"
    type = string
    default = "{sale_id}"
}

variable "region" {
    description = "AWS region"
    type = string
    default = "us-east-1"
}

variable "account_id" {
    description = "AWS account ID"
    type = string
}
