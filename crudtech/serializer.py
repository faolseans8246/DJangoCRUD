
from rest_framework import serializers
from .models import MyBase


# Serializer bilan ishlash
class MySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyBase
        fields = '__all__'