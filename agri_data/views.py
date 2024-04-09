from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ProfilAgriculteur  # Assurez-vous d'importer votre modèle ProfilAgriculteur
from .forms import ProfilAgriculteurForm


@login_required
def inscription_agriculteur(request):
    # Initialiser le formulaire avec les données existantes si le profil existe
    profil_agriculteur, created = ProfilAgriculteur.objects.get_or_create(utilisateur=request.user)
    if request.method == 'POST':
        form = ProfilAgriculteurForm(request.POST, instance=profil_agriculteur)
        if form.is_valid():
            form.save()
            # Redirection vers les services après mise à jour des données
            return redirect('agri_data:services')
    else:
        # Le formulaire est pré-rempli avec les informations de l'instance existante
        form = ProfilAgriculteurForm(instance=profil_agriculteur)
    return render(request, 'agri_data/inscription_agriculteur.html', {'form': form})

def soumettre_donnees(request):
    return render(request, 'agri_data/services.html')  # Assurez-vous que l'URL est correctement nommée dans vos fichiers urls.py

