from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Employee
from .forms import EmployeeForm, UserForm
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User


                                        ### CRUD Views ###


#Employee Create View

class EmpCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = EmployeeForm
    model = Employee
    success_url = reverse_lazy('EmployeeList:emp_create_view')


#Employee Retrive Views
#Employee List View

class EmpListView(ListView):
    model = Employee

    def get_queryset(self):
        return Employee.objects.all()
    

#Employee Detail View

class EmpDetailView(DetailView):
    model = Employee


#Employee Update View

class EmpUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    form_class = EmployeeForm
    model = Employee
    success_url = reverse_lazy('EmployeeList:emp_list_view')


#Employee Delete View

class EmpDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    success_url = reverse_lazy('EmployeeList:emp_list_view')


#New User Registration

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()


            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request,'registration/registration.html',
                            {'user_form': user_form,
                             'registered': registered})