data "aws_iam_policy_document" "policy_lambda_api" {
  statement {
    effect    = "Allow"
    actions   = [
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents"
    ]
    resources = ["arn:aws:logs:*:*:*"]
  }

  statement {
    effect    = "Allow"
    actions   = ["sqs:*"]
    resources = ["*"]
  }

  statement {
    effect = "Allow"
    actions = ["dynamodb:*"]
    resources = ["*"]
  }
}

data "aws_iam_policy_document" "policy_lambda_role" {
  statement {
    effect = "Allow"
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "lambda_api_role" {
  name               = "lambda_role"
  assume_role_policy = data.aws_iam_policy_document.policy_lambda_role.json
}

resource "aws_iam_policy" "lambda_api" {
  name        = "lambda_api_policy"
  policy      = data.aws_iam_policy_document.policy_lambda_api.json
  path        = "/"
  description = "IAM policy for logging from a lambda function"
}

resource "aws_iam_role_policy_attachment" "lambda_attachment" {
  role       = aws_iam_role.lambda_api_role.name
  policy_arn = aws_iam_policy.lambda_api.arn
}
