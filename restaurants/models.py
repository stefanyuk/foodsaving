import uuid
from django.db import models


class Restaurant(models.Model):
    """Schema to represent restaurant attributes in the database table."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    phone_number = models.CharField(max_length=15, verbose_name="phone number")
    email = models.EmailField(unique=True, verbose_name="email address")
    description = models.TextField()
