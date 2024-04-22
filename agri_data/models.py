from django.db import models
from django.conf import settings

class ProfilAgriculteur(models.Model):
    utilisateur = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    region = models.CharField(max_length=100)
    espace_travail = models.FloatField(null=True, default=None, help_text="Espace de travail en hectares")
    nombre_employes = models.IntegerField(null=True, default=0, help_text="Nombre d'employés")
    qualite_sol = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0.00, help_text="Budget en euros")
    produits = models.CharField(max_length=255, help_text="Liste des produits séparés par des virgules")
    periode_travail = models.CharField(max_length=100, help_text="Période de travail principale, ex : 'Janvier - Mars'")

    def __str__(self):
        return f"Profil de {self.utilisateur.username}"

class DonneesCapteur(models.Model):
    agriculteur = models.ForeignKey(ProfilAgriculteur, on_delete=models.CASCADE)
    date_heure = models.DateTimeField(auto_now_add=True)
    humidite = models.FloatField()
    temperature = models.FloatField()
    precipitation = models.FloatField()

    def __str__(self):
        return f"{self.date_heure.strftime('%Y-%m-%d %H:%M')} - Humidité: {self.humidite}%, Température: {self.temperature}°C"


class PrixProduit(models.Model):
    produit = models.CharField(max_length=100)
    date = models.DateField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    region = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f"{self.produit} le {self.date.strftime('%Y-%m-%d')} à {self.prix}€"

class RendementRegion(models.Model):
    region = models.CharField(max_length=100,null=True)
    date = models.DateField()
    rendement = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Rendement pour {self.region} le {self.date.strftime('%Y-%m-%d')} est de {self.rendement}"

 