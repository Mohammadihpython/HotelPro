from celery import shared_task


@shared_task()
def send_sms_code(phone_number: str, code: str) -> None:
    pass
