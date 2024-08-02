### IAM Policy for Lambda API
# iam policy document to lambda api
data "aws_iam_policy_document" "policy_lambda_api" {
  statement {
    effect = "Allow"
    actions = [
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
    effect    = "Allow"
    actions   = ["dynamodb:*"]
    resources = ["*"]
  }
}

# iam policy document to lambda role
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

# iam role lambda api
resource "aws_iam_role" "lambda_api_role" {
  name               = "lambda_role"
  assume_role_policy = data.aws_iam_policy_document.policy_lambda_role.json
}

# iam policy lambda api
resource "aws_iam_policy" "lambda_api" {
  name        = "lambda_api_policy"
  policy      = data.aws_iam_policy_document.policy_lambda_api.json
  path        = "/"
  description = "IAM policy for logging from a lambda function"
}

# iam policy attachment lambda api
resource "aws_iam_role_policy_attachment" "lambda_attachment" {
  role       = aws_iam_role.lambda_api_role.name
  policy_arn = aws_iam_policy.lambda_api.arn
}

### IAM Policy for Lambda Sales Processor
# iam policy document to lambda api
data "aws_iam_policy_document" "policy_lambda_sales_processor" {
  statement {
    effect = "Allow"
    actions = [
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
    effect    = "Allow"
    actions   = ["dynamodb:*"]
    resources = ["*"]
  }

  statement {
    effect    = "Allow"
    actions   = ["sns:*"]
    resources = ["*"]
  }

  statement {
    effect = "Allow"
    actions = [
      "events:*",
      "schemas:*",
      "scheduler:*",
      "pipes:*"
    ]
    resources = ["*"]
  }
}

# iam role lambda sales processor
resource "aws_iam_role" "lambda_sales_processor_role" {
  name               = "lambda_sales_processor_role"
  assume_role_policy = data.aws_iam_policy_document.policy_lambda_role.json
}

# iam policy
resource "aws_iam_policy" "lambda_sales_processor" {
  name        = "lambda_sales_processor_policy"
  policy      = data.aws_iam_policy_document.policy_lambda_sales_processor.json
  path        = "/"
  description = "IAM policy for logging from a lambda function"
}

# iam policy attachment sales processor
resource "aws_iam_role_policy_attachment" "lambda_sales_processor_attachment" {
  role       = aws_iam_role.lambda_sales_processor_role.name
  policy_arn = aws_iam_policy.lambda_sales_processor.arn
}
