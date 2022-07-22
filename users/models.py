import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from restaurants.models import Restaurant


class User(AbstractUser):
    """Schema to represent user attributes in the database table."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    phone_number = models.CharField(max_length=15, verbose_name="phone number")
    email = models.EmailField(unique=True, verbose_name="email address")
    is_active = models.BooleanField(
        verbose_name="Is user active",
        default=False,
        help_text="Designates whether this user should be treated as active."
                  "Unselect this instead of deleting accounts."
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-date_joined"]


class Post(models.Model):
    """Schema to represent post attributes in the database table."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_price = models.FloatField()
    discount = models.PositiveSmallIntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    available_quantity = models.PositiveSmallIntegerField()
    initial_quantity = models.PositiveSmallIntegerField()


class Review(models.Model):
    """Schema to represent review attributes in the database table."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    review_text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    """Schema to represent order attributes in the database table."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, blank=True, null=True)
    review = models.OneToOneField(Review, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)