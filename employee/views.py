from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import Employee_Form


def employee_data(request):
    emp = Employee_Form()

    if request.method == 'POST':
        emp = Employee_Form(request.POST or None)
        if emp.is_valid():
            emp.full_clean()
            emp.save()
            return HttpResponseRedirect(reverse_lazy(success))
        else:
            return render(request, 'employee/employee.html', {'form': emp})

    return render(request, 'employee/employee.html', {'form': emp})


def success(request):
    return render(request, 'employee/registered.html', {})
