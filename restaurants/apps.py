# pylint: disable=missing-module-docstring, missing-class-docstring
from django.apps import AppConfig


class RestaurantsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restaurants'
