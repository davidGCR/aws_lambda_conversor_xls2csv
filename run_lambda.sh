FUNC_NAME=test-xls
PACKAGE=fileb://deployment_package.zip
# PACKAGE=/c/Users/ZAT02/Documents/CODE/lambda_test_xls/deployment_package.zip
aws lambda update-function-code --function-name $FUNC_NAME --zip-file $PACKAGE