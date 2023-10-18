from django.db import models
from django.utils.translation import gettext_lazy as _
from .room_enums import STATUS, RoomType

# Create your models here.


class Room(models.Model):
    room_number = models.PositiveIntegerField(
        verbose_name=_("room_number"),
        unique=True,
    )
    status = models.CharField(
        verbose_name=_("status"),
        max_length=32,
        choices=STATUS.choices,
        default=STATUS.available,
    )
    price_per_day = models.DecimalField(
        verbose_name=_("price for one days"),
        max_digits=19,
        decimal_places=10,
        default=0,
    )
    room_type = models.CharField(
        verbose_name=_("room type"),
        max_length=100,
        choices=RoomType.choices,
        default=RoomType.standard_room,
    )
    detail = models.TextField(_("room detail"), blank=True, null=True)
    num_beds = models.PositiveIntegerField(
        verbose_name=_("count of the room beds"),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("product visibility"),
        help_text=_("format: Y-m-d H:M:S"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("date sub-product created"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    def __str__(self):
        return f"{self.room_number}-{self.status}"

    class Meta:
        verbose_name = _("room")
        verbose_name_plural = _("rooms")


class Media(models.Model):
    """
    The Room image table
    """

    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="media_room")
    image = models.ImageField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("room image"),
        upload_to="images/",
        default="images/default.png",
        help_text=_("format: required, default-default.png"),
    )
    alt_text = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("alternative text"),
        help_text=_("format: required, max-255"),
    )
    is_default = models.BooleanField(
        verbose_name=_("room default image"),
        help_text=_("format:default=false true=default image"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("product visibility"),
        help_text=_("format: Y-m-d H:M:S"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("date sub-product created"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    class Meta:
        verbose_name = _("room image")
        verbose_name_plural = _("room images")
