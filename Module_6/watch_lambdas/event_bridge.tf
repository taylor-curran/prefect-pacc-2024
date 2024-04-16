# resource "aws_cloudwatch_log_metric_filter" "lambda_start_filter" {
#   name           = "LambdaStartFilter"
#   pattern        = "START RequestId:"
#   log_group_name = aws_cloudwatch_log_group.lambda_log_group.name

#   metric_transformation {
#     name      = "LambdaStartCount"
#     namespace = "YourNamespace"
#     value     = "1"
#   }
# }
