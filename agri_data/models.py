from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class ProfilAgriculteur(models.Model):
    utilisateur = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    region = models.CharField(max_length=100)
    espace_travail = models.FloatField()  # en hectares, par exemple
    nombre_employes = models.IntegerField()
    qualite_sol = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    produits = models.CharField(max_length=255)  # Liste des produits séparés par des virgules
    periode_travail = models.CharField(max_length=100)  # Exemple: "Janvier - Mars"

    def __str__(self):
        return self.utilisateur.username

class DonneesCapteur(models.Model):
    agriculteur = models.ForeignKey(ProfilAgriculteur, on_delete=models.CASCADE)
    date_heure = models.DateTimeField(auto_now_add=True)
    humidite = models.FloatField()
    temperature = models.FloatField()
    precipitation = models.FloatField()

    def __str__(self):
        return f"{self.date_heure} - {self.agriculteur}"
