from rest_framework import viewsets
from .models import DonneesCapteur
from .serializers import DonneesCapteurSerializer

class DonneesCapteurViewSet(viewsets.ModelViewSet):
    queryset = DonneesCapteur.objects.all()
    serializer_class = DonneesCapteurSerializer

