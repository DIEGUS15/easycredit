from django.db import models
from products.models import Product
from clients.models import Client  # Importa el modelo Client


class Credit(models.Model):
    STATUS_CHOICES = [
        ('started', 'Started'),
        ('active', 'Active'),
        ('completed', 'Completed')
    ]
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='started')
    created_at = models.DateTimeField(auto_now_add=True)
    interest_rate_on_late_payments = models.DecimalField(
        max_digits=5, decimal_places=2)
    delinquent_payments = models.IntegerField(default=0)
    number_of_payments = models.IntegerField()
    total_credit = models.DecimalField(max_digits=10, decimal_places=2)

    # Relations
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="credits")
    Products = models.ManyToManyField(Product, related_name="credits")

    def __str__(self):
        # Esto mostrará la representación __str__ del objeto Client
        return str(self.client)


class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('delayed', 'Delayed')
    ]
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    due_in = models.DateTimeField()

    # Relation with Credit
    credit = models.ForeignKey(
        Credit, on_delete=models.CASCADE, related_name="payments")

    def __str__(self):
        return str(self.status)
