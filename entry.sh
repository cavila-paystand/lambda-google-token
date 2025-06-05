#!/bin/bash

if [ -z "${AWS_LAMBDA_RUNTIME_API}" ]; then
    # Local development
    exec /usr/local/bin/aws-lambda-rie /var/lang/bin/python3.9 -m awslambdaric $1
else
    # AWS Lambda
    exec /var/lang/bin/python3.9 -m awslambdaric $1
fi 