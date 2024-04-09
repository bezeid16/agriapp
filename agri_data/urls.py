from django.urls import path
from . import views
from .views import soumettre_donnees  # Assurez-vous d'avoir une vue correspondante

app_name = 'agri_data'

urlpatterns = [
    path('inscription/', views.inscription_agriculteur, name='inscription_agriculteur'),
    path('services/', soumettre_donnees, name='services')
]

