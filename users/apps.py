# pylint: disable=missing-module-docstring, missing-class-docstring
from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
