from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import Company_Form


def company_data(request):
    company = Company_Form()

    if request.method == 'POST':
        company = Company_Form(request.POST or None)
        if company.is_valid():
            company.full_clean()
            company.save()
            return HttpResponseRedirect(reverse_lazy(success))
        else:
            return render(request, 'company/company.html', {'form': company})

    return render(request, 'company/company.html', {'form': company})


def success(request):
    return render(request, 'company/registered.html', {})