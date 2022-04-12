#!/bin/sh
docker run --rm -d -p 6379:6379 --name celery-aws-xray-sdk-extension redis:alpine
celery -A tasks worker -n celery-aws-xray-sdk-extension-example -E -Q xray-demo -l INFO
docker stop celery-aws-xray-sdk-extension
