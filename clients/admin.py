from django.contrib import admin
from .models import Client

# CLIENT MODEL


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'email', 'phone_number', 'created_at']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['created_at']
