from django.urls import path
from . import views

urlpatterns = [
    path("employees/", views.employee_list, name="employee_list"),
    path("employees/create/", views.employee_create, name="employee_create"),
    path("employees/<int:pk>/update/", views.employee_update, name="employee_update"),
]