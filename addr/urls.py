from django.urls import path

from .views import addr_data, addr_list


urlpatterns = [
    path("", addr_data, name="index"),
    path("result/", addr_list, name="result"),
]
