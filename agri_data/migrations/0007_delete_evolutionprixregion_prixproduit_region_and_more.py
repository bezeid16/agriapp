# Generated by Django 4.2.8 on 2024-04-22 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri_data', '0006_evolutionprixregion_prixproduit_rendementregion_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EvolutionPrixRegion',
        ),
        migrations.AddField(
            model_name='prixproduit',
            name='region',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rendementregion',
            name='region',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
