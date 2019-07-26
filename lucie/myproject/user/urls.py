from django.urls import path
from .views import register_user, login_user, update_user


urlpatterns=[
path("register/", register_user, name="register_user"),
path("login/", login_user, name="login_user"),
path("update/", update_user, name="update_user"),
]
