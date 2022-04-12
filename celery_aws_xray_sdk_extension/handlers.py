from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core.utils import stacktrace
from aws_xray_sdk.ext.util import construct_xray_header, inject_trace_header

__all__ = (
    'xray_after_task_publish',
    'xray_before_task_publish',
    'xray_task_failure',
    'xray_task_postrun',
    'xray_task_prerun',
)

CELERY_NAMESPACE = 'celery'


def xray_before_task_publish(sender=None, headers=None, **kwargs):
    headers = headers if headers else {}
    task_id = headers.get('id')

    subsegment = xray_recorder.begin_subsegment(name=sender, namespace='remote')
    if not subsegment:
        return

    subsegment.put_metadata('task_id', task_id, namespace=CELERY_NAMESPACE)
    inject_trace_header(headers, subsegment)


def xray_after_task_publish(**kwargs):
    xray_recorder.end_subsegment()


def xray_task_prerun(task_id=None, task=None, **kwargs):
    xray_header = construct_xray_header(task.request)
    segment = xray_recorder.begin_segment(name=task.name, traceid=xray_header.root, parent_id=xray_header.parent)
    segment.save_origin_trace_header(xray_header)
    segment.put_annotation('routing_key', task.request.properties["delivery_info"]["routing_key"])
    segment.put_annotation('task_name', task.name)
    segment.put_metadata('task_id', task_id, namespace=CELERY_NAMESPACE)


def xray_task_postrun(**kwargs):
    xray_recorder.end_segment()


def xray_task_failure(exception=None, **kwargs):
    segment = xray_recorder.current_segment()
    if exception:
        stack = stacktrace.get_stacktrace(limit=xray_recorder._max_trace_back)
        segment.add_exception(exception, stack)
