from django.urls import path

from .views import user_account, index, register_user, user_login, ChangePasswordView


app_name = 'users'

urlpatterns = [
    path("home/", index, name="home"),
    path("account/", user_account, name="account"),
    path("register/", register_user, name="register_user"),
    path("login/", user_login, name="user_login"),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
]
