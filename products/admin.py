from django.contrib import admin
from .models import User, ProductType, Product, Credit, Payment

# USER MODEL


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'role', 'email']
    search_fields = ['username', 'email']
    list_filter = ['role']

# PRODUCTTYPE MODEL


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    search_fields = ['name']

# PRODUCT MODEL


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'reference', 'type', 'value', 'stock', 'status']
    search_fields = ['name', 'reference']
    list_filter = ['type', 'status']

# CREDIT MODEL


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ['client', 'product', 'created_at', 'status']
    search_fields = ['client_username', 'product_name']
    list_filter = ['status', 'created_at']

# PAYMENT MODEL


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['credit', 'value', 'due_in', 'status']
    search_fields = ['credit_client_username']
    list_filter = ['status', 'due_in']