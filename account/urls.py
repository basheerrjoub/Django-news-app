from django.urls import path
from .views import LogUser, LogoutViewUser, register

urlpatterns = [
    path("login", LogUser.as_view(), name="login"),
    path("logout/", LogoutViewUser.as_view(), name="logout"),
    path("register/", register, name="register"),
]
