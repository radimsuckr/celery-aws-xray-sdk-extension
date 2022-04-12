from pathlib import Path

from setuptools import find_packages, setup


def read_root_file(filename):
    root = Path('.')
    with open(root / filename, 'r') as f:
        return f.read().strip()


setup(
    name='celery-aws-xray-sdk-extension',
    # version=read_root_file('version'),
    author='Radim Sückr',
    author_email='kontakt@radimsuckr.cz',
    description='Extension for AWS X-Ray SDK which enables tracing of Celery tasks',
    long_description=read_root_file('readme.md'),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/druids/celery-aws-xray-sdk-extension',
    packages=find_packages(include=['celery_aws_xray_sdk_extension', 'tests']),
    install_requires=[
        'aws-xray-sdk>=2.9,<3',
        'celery>=5,<6',
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Celery',
        'License :: OSI Approved :: MIT License',
    ],
)
