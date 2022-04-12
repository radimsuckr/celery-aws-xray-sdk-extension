# Example for celery-aws-xray-sdk-extension

## Installation

[Docker](https://www.docker.com/) is required for this example setup.

1. Create an empty [virtualenv](https://virtualenv.pypa.io/en/latest/) in this directory and activate it.
2. Run `pip install -e .`in this directory.
3. Set environment variables to your testing AWS account (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_SESSION_TOKEN`).
4. Run `./run_xray_daemon.sh`. This starts in background a Docker container with AWS X-Ray daemon using latest version on port 2000.
5. Run `./run.sh`. This starts the Celery worker with AWS X-Ray SDK patch for `httplib`.

## Running demo Celery tasks

This demo project contains 3 Celery tasks: `add`, `power_2` and `complex`.

### Task `add`

`celery -A tasks call -a '[2, 2]' tasks.add`

Simply adds together two numbers. 

### Task `power_2`

`celery -A tasks call -a '[4]' tasks.power_2`

Returns second power of a number.

### Task `complex`

`celery -A tasks call -a '[2, 2]' tasks.complex`

Sends a HTTP request to [example.com](https://example.com/) and returns a second power of sum of two numbers.

`celery -A tasks call -a '[2, 2]' -k '{"fail": true}' tasks.complex`

You can optionally make it fail by providing `fail` kwarg set to `True`.
