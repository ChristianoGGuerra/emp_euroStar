from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import Company_Form
from .models import Comp_Info


def company_data(request):
    company = Company_Form()

    if request.method == 'POST':
        company = Company_Form(request.POST or None)
        if company.is_valid():
            company.full_clean()
            company.save()
            return HttpResponseRedirect(reverse_lazy(company_list))
        else:
            return render(request, 'company/company.html', {'form': company})

    return render(request, 'company/company.html', {'form': company})

def company_list(request):
    company = Comp_Info.objects.all()
    return render(request, "company/registered.html", {"company": company})