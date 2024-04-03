from django.forms import ModelForm
from .models import ProfilAgriculteur

class ProfilAgriculteurForm(ModelForm):
    class Meta:
        model = ProfilAgriculteur
        fields = ['region', 'espace_travail', 'nombre_employes', 'qualite_sol', 'budget', 'produits', 'periode_travail']
