from django.urls import path

from .views import (
    addr_data,
    success)


urlpatterns = [
    path("", addr_data, name="index"),
    path("success/", success, name="success"),
]
