from rest_framework import serializers  # , viewsets
from .models import Client

# Serializer for Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
