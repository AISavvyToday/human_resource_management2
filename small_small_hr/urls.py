from django.urls import path
from . import views



urlpatterns = [
    path('apply-leave/', views.ApplyLeave , name='apply-leave'),
    path('create-staff/', views.CreateStaff , name='create-staff'),
    path('annual-leave/', views.ManageAnnualLeave , name='annual-leave'),
    path('role-form/', views.ManageRoles , name='role-form'),
    path('holiday-form/', views.ManageHolidays , name='holiday-form')


]
    