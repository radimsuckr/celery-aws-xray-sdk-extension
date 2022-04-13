# celery-aws-xray-sdk-extension

[![PyPI version](https://img.shields.io/pypi/v/celery-aws-xray-sdk-extension)](https://pypi.org/project/celery-aws-xray-sdk-extension/) ![PyPI license](https://img.shields.io/pypi/l/celery-aws-xray-sdk-extension)

Celery signal handlers that integrate Celery task lifecycle with AWS X-Ray tracing.

There's a tiny example in the directory `example`.

## Installation

You can install it easily with `pip`: `pip install celery-aws-xray-sdk-extension`. For latest version visit [PyPI](https://pypi.org/project/celery-aws-xray-sdk-extension/).

## Setup

This guide doesn't cover setting up AWS X-Ray SDK for Python or AWS X-Ray daemon. It's expected that you've already got some experience with it. If you don't have any experience with AWS X-Ray, please visit [Amazon documentation](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html).

1. You have to have [Celery signals](https://docs.celeryq.dev/en/stable/userguide/signals.html) enabled.
2. Connect Celery signals to signal handlers from `celery_aws_xray_sdk_extension` module in your Celery setup. Example code is below this list.
3. You're good to go!

### Connecting handlers to Celery signals

```python
signals.after_task_publish.connect(xray_after_task_publish)
signals.before_task_publish.connect(xray_before_task_publish)
signals.task_failure.connect(xray_task_failure)
signals.task_postrun.connect(xray_task_postrun)
signals.task_prerun.connect(xray_task_prerun)
```

## Development

Before making any changes, please prepare your environment (no global changes are made!) with `make setup-dev`. Feel free to check what the target does in the `Makefile`.

This repository uses [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
