from celery import shared_task
from . import models
import datetime
from django.utils import timezone


# @shared_task()
def send_sms_code(phone_number: str, code: str) -> None:
    print(code)


# @shared_task
def verify_sms(phone_number, code):
    user = models.UserOTP.objects.filter(phone_number=phone_number).last()
    if user.code == code and user.time_in_range(
        user.expire_time_start, user.expire_time_end, timezone.make_aware(datetime.datetime.now())
    ):
        return True
    else:
        return False
