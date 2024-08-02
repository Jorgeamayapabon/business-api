variable "lambda_function_name" {
  description = "name of the lambda function"
  type        = string
  default     = "business_api"
}

variable "lambda_sales_processor_name" {
  description = "name of the lambda sales processor function"
  type        = string
  default     = "sales_processor"
}

variable "users_path" {
  description = "path for the users resource"
  type        = string
  default     = "users"
}

variable "user_id_path" {
  description = "path for the user id resource"
  type        = string
  default     = "{user_id}"
}

variable "clients_path" {
  description = "path for the clients resource"
  type        = string
  default     = "clients"

}

variable "client_id_path" {
  description = "path for the client id resource"
  type        = string
  default     = "{client_id}"
}

variable "sales_path" {
  description = "path for the sales resource"
  type        = string
  default     = "sales"
}

variable "sale_id_path" {
  description = "path for the sale id resource"
  type        = string
  default     = "{sale_id}"
}

variable "account_id" {
  description = "AWS account ID"
  type        = string
}

variable "table_user_name" {
  description = "Name of the user table"
  type        = string
  default     = "user"
}

variable "table_client_name" {
  description = "Name of the client table"
  type        = string
  default     = "client"
}

variable "table_sale_name" {
  description = "Name of the sale table"
  type        = string
  default     = "sale"
}

variable "queue_sale_processor_name" {
  description = "Name of the queue for the sales processor"
  type        = string
}

variable "sns_event_topic_name" {
  description = "Name of the SNS topic for the sales processor"
  type        = string
}

variable "region" {
  description = "AWS region"
  type        = string
}