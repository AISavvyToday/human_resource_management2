from django.urls import path
from . import views



urlpatterns = [

    path('apply-leave/', views.ApplyLeave , name='apply-leave'),
    path('apply-overtime/', views.ApplyOverTime , name='apply-overtime')

]