from django.urls import path
from . import views

app_name = 'agri_data'

urlpatterns = [
    path('inscription/', views.inscription_agriculteur, name='inscription_agriculteur'),
]
