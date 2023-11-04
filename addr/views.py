from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import Addr_Form
from .models import Addr_Info


def addr_data(request):
    address = Addr_Form()

    if request.method == 'POST':
        address = Addr_Form(request.POST or None)
        if address.is_valid():
            address.full_clean()
            address.save()
            return HttpResponseRedirect(reverse_lazy(addr_list))
        else:
            return render(request, 'addr/addr.html', {'form': address})

    return render(request, 'addr/addr.html', {'form': address})

def addr_list(request):
    addr = Addr_Info.objects.all()
    return render(request, "addr/registered.html", {"address": addr})

def success(request):
    return render(request, 'addr/registered.html', {})
