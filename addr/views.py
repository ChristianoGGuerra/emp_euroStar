from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import Addr_Form


def addr_data(request):
    address = Addr_Form()

    if request.method == 'POST':
        address = Addr_Form(request.POST or None)
        if address.is_valid():
            address.full_clean()
            address.save()
            return HttpResponseRedirect(reverse_lazy(success))
        else:
            return render(request, 'addr/addr.html', {'form': address})

    return render(request, 'addr/addr.html', {'form': address})


def success(request):
    return render(request, 'addr/registered.html', {})
