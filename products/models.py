from django.contrib.auth.models import AbstractUser
from django.db import models

# USERS MODEL


class User(AbstractUser):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('employee', 'Employee'),
        ('admin', 'Admin')
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Agregamos related_name para evitar el conflicto
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_permission_set',  # También agregamos related_name aquí
        blank=True
    )

    def __str__(self) -> str:
        return f"{self.username} ({self.role})"

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

# PRODUCT MODEL


class Product(models.Model):
    STATUSES = {
        "active": "Active",
        "inactive": "Inactive"
    }
    reference = models.CharField(max_length=127)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    # provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=511)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField()
    status = models.CharField(max_length=55, choices=STATUSES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)

# CREDIT MODEL

