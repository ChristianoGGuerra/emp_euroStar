from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from addr.models import Addr_Info
from company.models import Comp_Info


class Employee_Info(models.Model):
    company_number = models.IntegerField(primary_key=True, unique=True, validators=[MinValueValidator(1), MaxValueValidator(500)])
    start_date = models.DateField()
    prefix = models.CharField(max_length=4, blank=True)
    name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True)
    mobile_phone = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=150, validators=[EmailValidator()])
    area_of_work = models.CharField(max_length=150, blank=True)
    disabled = models.BooleanField(blank=True)
    # address = models.ForeignKey("addr.Addr_Info", on_delete=models.CASCADE)
    # company = models.ForeignKey("company.Comp_Info", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.company_number) + ' - ' + self.name + ' ' + self.last_name + ' --> ' + self.email
