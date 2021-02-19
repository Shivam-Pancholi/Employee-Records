from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'EmployeeList'

urlpatterns = [
    path('', views.EmpListView.as_view(), name='emp_list_view'),
    path('register/', views.register, name='register'),
    path('employee/<int:pk>', views.EmpDetailView.as_view(), name='emp_detail_view'),
    path('employee/new', views.EmpCreateView.as_view(), name='emp_create_view'),
    path('employee/<int:pk>/edit', views.EmpUpdateView.as_view(), name='emp_update_view'),
    path('employee/<int:pk>/remove', views.EmpDeleteView.as_view(), name='emp_delete_view'),
    path('accounts/login/', LoginView.as_view(), name='login', kwargs={'next': '/'}),
    path('accounts/logout/', LogoutView.as_view(), name='logout', kwargs={'next  ': '/'}),
]