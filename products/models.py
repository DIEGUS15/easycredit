# from django.conf import settings  # Importa el modelo de usuario personalizado
from django.db import models


# PRODUCTTYPE MODEL


class ProductType(models.Model):
    STATUSES = {
        "active": "Active",
        "inactive": "Inactive"
    }
    name = models.CharField(max_length=511, null=False)
    status = models.CharField(max_length=55, choices=STATUSES)

    def __str__(self) -> str:
        return str(self.name)


# PROVIDER MODEL


class Provider(models.Model):
    STATUSES = {
        "active": "Active",
        "inactive": "Inactive"
    }
    name = models.CharField(max_length=511, null=False)
    status = models.CharField(max_length=55, choices=STATUSES)

    def __str__(self) -> str:
        return str(self.name)

# PRODUCT MODEL


class Product(models.Model):
    STATUSES = {
        "active": "Active",
        "inactive": "Inactive"
    }
    reference = models.CharField(max_length=127)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    provider = models.ForeignKey(
        Provider, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=511)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField()
    status = models.CharField(max_length=55, choices=STATUSES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(
    #     # Se usa settings.AUTH_USER_MODEL para referirse al modelo de usuario actual
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.RESTRICT,
    #     related_name='products',
    #     null=True
    # )

    def __str__(self) -> str:
        return str(self.name)
