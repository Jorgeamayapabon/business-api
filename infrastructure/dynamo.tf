resource "aws_dynamodb_table" "table_user" {
  name           = var.table_user_name
  billing_mode   = "PROVISIONED"
  read_capacity  = 1
  write_capacity = 1
  hash_key       = "user_id"

  attribute {
    name = "user_id"
    type = "S"
  }
}

resource "aws_dynamodb_table" "table_client" {
  name           = var.table_client_name
  billing_mode   = "PROVISIONED"
  read_capacity  = 1
  write_capacity = 1
  hash_key       = "client_id"

  attribute {
    name = "client_id"
    type = "S"
  }
}

resource "aws_dynamodb_table" "table_sale" {
  name           = var.table_sale_name
  billing_mode   = "PROVISIONED"
  read_capacity  = 1
  write_capacity = 1
  hash_key       = "sale_id"

  attribute {
    name = "sale_id"
    type = "S"
  }
}
