import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Schema to represent user attributes in the database table."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    phone_number = models.CharField(max_length=15, verbose_name="phone number")
    email = models.EmailField(unique=True, verbose_name="email address")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-date_joined"]
