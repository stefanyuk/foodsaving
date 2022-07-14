from django.urls import path

from .views import register_user, index, activate_user_profile, user_login


app_name = 'users'

urlpatterns = [
    path("register/", register_user, name="register_user"),
    path("home/", index, name="home"),
    path("activate/<uidb64>/<token>", activate_user_profile, name="activate"),
    path("login/", user_login, name="user_login")
]
