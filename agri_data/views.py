from django.shortcuts import render, redirect
from .forms import ProfilAgriculteurForm

def inscription_agriculteur(request):
    if request.method == 'POST':
        form = ProfilAgriculteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agri_data:home')  # Redirige vers la page d'accueil après une inscription réussie
    else:
        form = ProfilAgriculteurForm()
    return render(request, 'agri_data/inscription_agriculteur.html', {'form': form})
