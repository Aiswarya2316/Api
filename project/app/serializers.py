from rest_framework import serializers
from .models import *

# class sample(serializers.Serializer):
#     name=serializers.CharField()
#     address=serializers.CharField()
#     position=serializers.CharField()
#     salary=serializers.IntegerField()
#     experiance=serializers.CharField()
#     phone=serializers.CharField()
#     email=serializers.CharField()
#     empid=serializers.CharField()


class model_serializers(serializers.ModelSerializer):
    class Meta:
        model=employe
        fields='__all__'