from django.urls import path

from .views import (company_data,
                    success)


urlpatterns = [
    path("", company_data, name="index"),
    path("success/", success, name="success"),
]
