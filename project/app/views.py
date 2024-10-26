from rest_framework import viewsets
from .models import *
from .serializers import model_serializers

# class model_serializer(viewsets.ModelViewSet):
#     queryset = employe.objects.all()
#     serializer_class = model_serializers


class model_serializerr(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = model_serializers