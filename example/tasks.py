import requests
from aws_xray_sdk.core.patcher import patch
from celery import Celery, signals

from celery_aws_xray_sdk_extension.handlers import (xray_after_task_publish,
                                                    xray_before_task_publish,
                                                    xray_task_failure,
                                                    xray_task_postrun,
                                                    xray_task_prerun)

patch(('httplib',))

app = Celery(backend='redis://localhost:6379/1', broker='redis://localhost:6379/0')
app.conf.task_default_queue = 'xray-demo'

signals.after_task_publish.connect(xray_after_task_publish)
signals.before_task_publish.connect(xray_before_task_publish)
signals.task_failure.connect(xray_task_failure)
signals.task_postrun.connect(xray_task_postrun)
signals.task_prerun.connect(xray_task_prerun)


@app.task
def add(x, y):
    return x + y


@app.task
def power_2(self, x):
    return x ** 2


@app.task
def complex(x, y, fail=False):
    requests.get('https://example.com')
    add.apply_async((2, 2), link=power_2.s())
    if fail:
        raise Exception('A really serious bug')
