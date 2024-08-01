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

variable "region" {
    description = "AWS region"
    type = string
    default = "us-east-1"
}

variable "account_id" {
    description = "AWS account ID"
    type = string
}
