from django import forms
from django.core import validators

from .models import Addr_Info, Country_List


class Addr_Form(forms.ModelForm):
    def clean(self):
        clean_data = super(Addr_Form, self).clean()

    zip_code = forms.CharField(validators=[validators.RegexValidator('^(^[0-9]{4}(?:-[0-9]{3})?$|^$)')])

    class Meta:
        model = Addr_Info
        fields = [
            'address_line1',
            'number',
            'others',
            'city',
            'county',
            'country',
            'zip_code'
        ]
