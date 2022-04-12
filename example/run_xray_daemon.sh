#!/bin/sh
docker run --name aws-xray-daemon --rm -d -p 2000:2000 -e AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} -e AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} -e AWS_SESSION_TOKEN=${AWS_SESSION_TOKEN} --network host public.ecr.aws/xray/aws-xray-daemon:latest -o -n eu-central-1
