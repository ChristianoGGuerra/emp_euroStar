from django import forms
from django.core import validators

from .models import Comp_Info


class Company_Form(forms.ModelForm):
    def clean(self):
        clean_data = super(Company_Form, self).clean()

    url = forms.CharField(validators=[validators.URLValidator(message='This url is not valid.')])

    class Meta:
        model = Comp_Info
        fields = [
            'identify',
            'name',
            'url',
            'contact',
            'activity',
            'address'
        ]
