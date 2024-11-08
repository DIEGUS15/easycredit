from rest_framework import serializers  # , viewsets
from .models import Credit, Payment
from products.serializers import ProductSerializer
from clients.serializers import ClientSerializer


class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
