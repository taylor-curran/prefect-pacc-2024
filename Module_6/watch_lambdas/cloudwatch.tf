
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
