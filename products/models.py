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

class Credit(models.Model):
    # this is not necesary the error is for the linter
    # id = models.AutoField(primary_key=True)
    STATUS_CHOICES = [
        ('started', 'Started'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]
    client = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={
                               'role': 'client'})  # Only clients can have credits
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    # def _str_(self):
    #     return f"Credit {self.pk} for {self.client.username}"
    def str(self):
        return f"Credit {self.id} for {self.client.username}"

# PAYMENT MODEL


class Payment(models.Model):
    # this is not necesary the error is for the linter
    id = models.AutoField(primary_key=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('delayed', 'Delayed'),
    ]
    credit = models.ForeignKey(Credit, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    due_in = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    # def _str_(self):
    #     return f"Payment {self.pk} for Credit {self.credit.pk}"
    def str(self):
        return f"Payment {self.id} for Credit {self.credit.id}"