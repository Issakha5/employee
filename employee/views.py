from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .serializers import EmployeeSerializer


def employees_list(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'employee/list.html', context)


def create_employee(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees-list')

    context = {
        'form': form,
    }
    return render(request, 'employee/create.html', context)


def edit_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees-list',)

    context = {
        'employee': employee,
        'form': form,
    }
    return render(request, 'employee/edit.html', context)


def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('employees-list')

    context = {
        'employee': employee,
    }
    return render(request, 'employee/delete.html', context)

class EmployeeList(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.AllowAny, )


class EmployeeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.AllowAny, )
