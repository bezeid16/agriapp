# agriapp/urls.py

from django.contrib import admin
from django.urls import path, include  # Assurez-vous d'importer include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),  # Ajoutez cette ligne
    path('agri_data/', include('agri_data.urls')),
]
