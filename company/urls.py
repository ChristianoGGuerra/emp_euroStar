from django.urls import path

from .views import (company_data,
                    company_list)


urlpatterns = [
    path("", company_data, name="index"),
    path("result/", company_list, name="result"),
]
