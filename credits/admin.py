from django.contrib import admin
from .models import Credit, Payment


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ('client', 'status', 'created_at',
                    'number_of_payments', 'total_credit')
    list_filter = ('status', 'created_at')
    search_fields = ('client__first_name',
                     'client__last_name', 'client__email')
    filter_horizontal = ('Products',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('credit', 'status', 'value', 'due_in')
    list_filter = ('status', 'due_in')
    search_fields = ('credit__client__first_name',
                     'credit__client__last_name', 'credit__client__email')
