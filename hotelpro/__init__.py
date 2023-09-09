"""
To make sure that your Celery app is loaded when you start Django,
you should add it to __all__:
"""
from .celery import app as celery_app


__all__ = ("celery_app",)
