from django import forms
from django.core import validators

from .models import Employee_Info


class Employee_Form(forms.ModelForm):
    def clean(self):
        clean_data = super(Employee_Form, self).clean()

    company_number = forms.IntegerField(validators=[validators.MinValueValidator(1),
                                                    validators.MaxValueValidator(500)])

    class Meta:
        model = Employee_Info
        fields = [
            'company_number',
            'start_date',
            'prefix',
            'name',
            'middle_name',
            'last_name',
            'date_of_birth',
            'mobile_phone',
            'email',
            'area_of_work',
            'address',
            'company',
            'disabled',
        ]
