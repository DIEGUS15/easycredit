from django.contrib import admin
from .models import ProductType, Product, Provider


# PRODUCTTYPE MODEL
@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    search_fields = ['name']


# PROVIDER MODEL
@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    search_fields = ['name']

# PRODUCT MODEL


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'reference', 'type', 'value', 'stock', 'status']
    search_fields = ['name', 'reference']
    list_filter = ['type', 'status']
