from rest_framework import viewsets
from .models import employe
from .serializers import model_serializers

class model_serializer(viewsets.ModelViewSet):
    queryset = employe.objects.all()
    serializer_class = model_serializers