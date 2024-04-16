provider "aws" {
  region = "us-west-2" # or your preferred region
}

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
  bucket = "taylor-lambda-function-bucket" # Update this line with your bucket name
  acl    = "private"
}

resource "aws_s3_bucket_object" "lambda_object" {
  bucket = aws_s3_bucket.lambda_bucket.bucket
  key    = "lambda_function.zip" # This should match the name of your ZIP file
  source = "~/Documents/tay/prefect-pacc-2024/Module_6/watch_lambdas/lambda_function.zip" # Local path to your ZIP file
  etag   = filemd5("~/Documents/tay/prefect-pacc-2024/Module_6/watch_lambdas/lambda_function.zip") # This calculates the MD5 hash of your ZIP file
}

resource "aws_lambda_function" "my_lambda" {
  function_name = "MyRandomSleepFunction"

  s3_bucket = aws_s3_bucket.lambda_bucket.bucket
  s3_key    = aws_s3_bucket_object.lambda_object.key

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
