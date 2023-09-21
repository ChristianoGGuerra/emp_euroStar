from django import forms
from django.forms import ModelForm
from .models import Addr_Info


class AddrForm(ModelForm):
    class Meta:
        model = Addr_Info
        fields = '__all__'
