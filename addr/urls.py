from django.urls import path

from .views import addr_data


urlpatterns = [
    path("", addr_data, name="index"),
]
