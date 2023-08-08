# trainee_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('trainee/', views.trainee_form, name='trainee_form'),
    path('success/', views.success, name='success'),
]