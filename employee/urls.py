from django.urls import path

from .views import (
    employee_data,
    success)


urlpatterns = [
    path("", employee_data, name="index"),
    path("success/", success, name="success"),
]
