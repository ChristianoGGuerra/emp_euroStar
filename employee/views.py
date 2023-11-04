from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import Employee_Form
from .models import Employee_Info


def employee_data(request):
    emp = Employee_Form()

    if request.method == 'POST':
        emp = Employee_Form(request.POST or None)
        if emp.is_valid():
            emp.full_clean()
            emp.save()
            return HttpResponseRedirect(reverse_lazy(employee_list))
        else:
            return render(request, 'employee/employee.html', {'form': emp})

    return render(request, 'employee/employee.html', {'form': emp})

def employee_list(request):
    emp = Employee_Info.objects.all()
    return render(request, "employee/results.html", {"employee": emp})


def success(request):
    return render(request, 'employee/registered.html', {})
