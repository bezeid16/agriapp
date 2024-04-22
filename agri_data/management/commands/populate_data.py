# agri_data/management/commands/populate_data.py
 
from django.core.management.base import BaseCommand
from agri_data.models import PrixProduit, RendementRegion
import pandas as pd
import numpy as np
from datetime import datetime
from django.utils import timezone

class Command(BaseCommand):
    help = 'Generates and inserts random data into PrixProduit and RendementRegion models.'

    def handle(self, *args, **options):
        self.generate_data()
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with random data.'))

    def generate_data(self):
        n_observations = 1000  # Nombre d'observations à générer
        regions = [
            'Hodh Chargui', 'Hodh El Gharbi', 'Assaba', 'Gorgol', 'Brakna', 'Trarza',
            'Adrar', 'Dakhlet Nouadhibou', 'Tagant', 'Guidimakha', 'Tiris Zemmour',
            'Inchiri', 'Nouakchott'
        ]
        produits = [
            'Blé', 'Maïs', 'Sorgho', 'Riz', 'Millet', 'Orge', 'Coton', 'Arachide',
            'Tomate', 'Pastèque', 'Pomme de terre', 'Oignon', 'Ail', 'Fruit de palme', 'Patate douce'
        ]

        # Génération des dates aléatoires entre 2014 et 2023
        dates = pd.date_range(start="2014-01-01", end="2023-12-31", freq='D')
        random_dates = np.random.choice(dates, n_observations)

        # Génération aléatoire des autres données
        region_data = np.random.choice(regions, n_observations)
        produit_data = np.random.choice(produits, n_observations)
        prix_data = np.random.uniform(low=10.0, high=100.0, size=n_observations)
        rendement_data = np.random.uniform(low=100.0, high=1000.0, size=n_observations)

        # Insertion des données dans la base de données
        for i in range(n_observations):
            dt = pd.to_datetime(str(random_dates[i]))  # Conversion en datetime.datetime
            dt_aware = timezone.make_aware(dt)  # Rendre la date consciente de la zone horaire

            PrixProduit.objects.create(
                produit=produit_data[i],
                date=dt_aware,
                prix=prix_data[i],
                region=region_data[i]
            )
            RendementRegion.objects.create(
                region=region_data[i],
                date=dt_aware,
                rendement=rendement_data[i]
            )
