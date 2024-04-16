aws sso login

zip lambda_function.zip lambda_function.py

aws lambda invoke \
--function-name MyRandomSleepFunction \
--payload '{}' \
response.json

