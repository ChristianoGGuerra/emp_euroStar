from django.urls import path

from .views import (
    employee_data,
    employee_list)


urlpatterns = [
    path("", employee_data, name="index"),
    path("result/", employee_list, name="result"),
]
