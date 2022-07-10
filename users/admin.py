from django.contrib import admin

from .models import User


class UsersAdmin(admin.ModelAdmin):
    """Class to represent Django admin configuration for user application."""

    list_display = (
        "email",
        "phone_number",
        "first_name",
        "last_name",
        "is_staff",
        "date_joined",
    )
    list_display_links = ("email",)
    list_editable = ("is_staff",)
    list_filter = ("is_staff",)
    search_fields = ("email", "first_name", "last_name")


admin.site.register(User, UsersAdmin)
