from random import choice
from django.db import models
from room.models import Room
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()



class STATUS(models.TextChoices):
    pending = ("pending","pending")
    confirmed = ("confirmed", "confirmed")
    cancelled = ("cancelled", "cancelled")
    completed = ("completed", "completed")


class Booking(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE,related_name='reservations') # type: ignore
    check_in =models.DateTimeField(_("start date of stay"))
    check_out = models.DateTimeField(_("end data of stay"))
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='reservations')
    status = models.CharField(verbose_name=_("reservation status"),max_length=100, choices=STATUS.choices,default=STATUS.pending)# type: ignore

    @property
    def total_cost(self):
        duration = self.check_out - self.check_in
        num_nights = duration.days
        per_night_price = self.room.price_per_day

        return num_nights * per_night_price
