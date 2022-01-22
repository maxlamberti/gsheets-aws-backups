# gsheets-aws-backups

![python version](https://img.shields.io/badge/python-3.6-blue.svg)

## Description

Back up google sheets to S3 bucket using a Lambda function.

## Prerequisites

1. An existing lambda function and S3 bucket.
2. A set of google service account credentials to read the google sheet.
3. Add environment variables SHEET_TITLE and S3_BUCKET to the lambda function, cointaining the name of the Google sheet and the name of the S3 bucket, respectively.

## Build And Deployment

Place the google credentials in the project directory as `google_credentials.json`.

Build the deployment package by executing the `build.sh` script in the project directory.

Upload the `deployment.zip` file to the lambda function through the aws management console or deploy in the aws cli:

```
aws lambda update-function-code \
    --function-name FUNCTION_NAME \
    --zip-file fileb:///path/to/gsheets-aws-backups/deployment.zip
```
