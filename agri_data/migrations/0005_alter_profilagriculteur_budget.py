# Generated by Django 4.2.8 on 2024-04-19 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri_data', '0004_alter_profilagriculteur_nombre_employes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilagriculteur',
            name='budget',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
