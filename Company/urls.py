from django.contrib import admin
from django.urls import path, include
from EmployeeList import views
urlpatterns = [
    path('', include('EmployeeList.urls')),
    path('admin/', admin.site.urls),
]
