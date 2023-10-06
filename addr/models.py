from django.db import models


class Addr_Info(models.Model):
    address_line1 = models.CharField(max_length=250)
    number = models.IntegerField(blank=True)
    others = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150)
    county = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return (self.address_line1 + ' - ' + str(self.number) + ' ' + self.others + ' --> '
                + self.city + ' - ' + self.county + ' - ' + self.country)
