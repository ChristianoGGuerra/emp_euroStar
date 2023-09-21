from django.db import models
from addr.models import Addr_Info


class Comp_Info(models.Model):
    identify = models.Field(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    url = models.EmailField(max_length=255, blank=True)
    contact = models.CharField(max_length=150)
    activity = models.CharField(max_length=250)
    address = models.ForeignKey("addr.Addr_Info", on_delete=models.CASCADE)
