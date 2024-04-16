aws sso login

zip lambda_function.zip lambda_function.py

aws lambda invoke \
--function-name MyRandomSleepFunction \
--payload '{}' \
response.json

terraform import aws_cloudwatch_log_group.lambda_log_group /aws/lambda/MyRandomSleepFunction
