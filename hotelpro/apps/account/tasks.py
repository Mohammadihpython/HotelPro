from celery import shared_task
from . import models
import datetime
from django.utils import timezone
from typing import List
from .utils import sms
@shared_task()
def send_sms_code(phone_number:str |List[str], code) -> None:
    message = f":کد ورود برای سایت هتل حرفه ایی{code}"

    sms.send(phone_number,message=message)


@shared_task
def verify_sms(phone_number, code):
    user = models.UserOTP.objects.filter(phone_number=phone_number).first()
    return bool(
        user.code == code
        and user.time_in_range(
            user.expire_time_start,
            user.expire_time_end,
            timezone.make_aware(datetime.datetime.now()),
        )
    )
