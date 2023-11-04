from django.db import models


class Country_List(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    population = models.CharField(max_length=15)
    area_km2 = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Addr_Info(models.Model):
    address_line1 = models.CharField(max_length=250)
    number = models.IntegerField(blank=True)
    others = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150)
    county = models.CharField(max_length=150)
    country = models.ForeignKey(Country_List, on_delete=models.SET_NULL, null=True)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return (self.address_line1 + ' - ' + str(self.number) + ' ' + self.others + ' --> '
                + self.city + ' - ' + self.county )
