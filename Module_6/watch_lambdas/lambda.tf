resource "aws_iam_role" "lambda_execution_role" {
  name = "lambda_execution_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        },
      },
    ]
  })
}

resource "aws_s3_bucket" "lambda_bucket" {
  bucket = "taylor-lambda-function-bucket"
  acl    = "private"
}

resource "aws_s3_object" "lambda_object" {
  bucket = aws_s3_bucket.lambda_bucket.bucket
  key    = "lambda_function.zip"
  source = "~/Documents/bs/prefect-pacc-2024/Module_6/watch_lambdas/lambda_function.zip"
  etag   = filemd5("~/Documents/bs/prefect-pacc-2024/Module_6/watch_lambdas/lambda_function.zip")
}

resource "aws_lambda_function" "my_lambda" {
  function_name = "MyRandomSleepFunction"

  s3_bucket = aws_s3_bucket.lambda_bucket.bucket
  s3_key    = aws_s3_object.lambda_object.key

  handler = "lambda_function.lambda_handler"
  runtime = "python3.10"
  role    = aws_iam_role.lambda_execution_role.arn

  timeout = 60 # Adjust as needed
}
# You may need to add additional permissions to your IAM role depending on what your Lambda needs to do.
resource "aws_iam_policy" "lambda_policy" {
  name        = "lambda_policy"
  description = "A test policy for our lambda"
  policy      = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "lambda_logs" {
  role       = aws_iam_role.lambda_execution_role.name
  policy_arn = aws_iam_policy.lambda_policy.arn
}

# CloudWatch Stuff

resource "aws_cloudwatch_log_group" "lambda_log_group" {
  name = "/aws/lambda/${aws_lambda_function.my_lambda.function_name}"
}

# resource "aws_cloudwatch_metric_alarm" "lambda_start_alarm" {
#   alarm_name                = "LambdaStartAlarm"
#   comparison_operator       = "GreaterThanThreshold"
#   evaluation_periods        = "1"
#   metric_name               = aws_cloudwatch_log_metric_filter.lambda_start_filter.metric_transformation.name
#   namespace                 = aws_cloudwatch_log_metric_filter.lambda_start_filter.metric_transformation.namespace
#   period                    = 60
#   statistic                 = "Sum"
#   threshold                 = "0"
#   alarm_description         = "Triggered when the Lambda function starts"
#   actions_enabled           = true
#   alarm_actions             = [aws_sns_topic.lambda_trigger_sns.arn]
# }
