from rest_framework import viewsets
from .models import Credit, Payment
from .serializers import CreditSerializer, PaymentSerializer


class CreditViewSet(viewsets.ModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
