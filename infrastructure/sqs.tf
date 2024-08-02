resource "aws_sqs_queue" "queue_sale_processor" {
  name                        = var.queue_sale_processor_name
  fifo_queue                  = true
  content_based_deduplication = true
  visibility_timeout_seconds = 60
  message_retention_seconds = 3600
  max_message_size = 262144
}
