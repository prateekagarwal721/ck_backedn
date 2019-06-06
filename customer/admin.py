from django.contrib import admin
from django_extensions.admin import ForeignKeyAutocompleteAdmin
from customer.models import Customer

# Register your models here.
class CustomerAdmin(ForeignKeyAutocompleteAdmin):
    model = Customer

admin.site.register(Customer,CustomerAdmin)