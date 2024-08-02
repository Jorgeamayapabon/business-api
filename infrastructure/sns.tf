resource "aws_sns_topic" "notification" {
    name = "notification"
}

resource "aws_sns_topic_subscription" "subscription_email" {
    topic_arn = aws_sns_topic.notification.arn
    protocol  = "email"
    endpoint  = "jeap1723@gmail.com"
}
