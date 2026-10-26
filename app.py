# Source reference for the Lambda code embedded in expense-tracker.yaml.
# The deployed function is defined inline in CloudFormation so the stack can be
# deployed directly without building or uploading a ZIP package.
#
# API:
#   POST /expenses  JSON: {"amount": 12.50, "category": "Food", "description": "Lunch"}
#   GET  /expenses  returns saved expense records
#
# The deployed function uses DynamoDB for persistence and CloudWatch Logs for
# runtime logging. It labels the project output "Berlyn's Expense Tracker".
