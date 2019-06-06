from django.contrib import admin
from django_extensions.admin import ForeignKeyAutocompleteAdmin
from address.models import CustomerAddress

# Register your models here.
class CustomerAddressAdmin(ForeignKeyAutocompleteAdmin):
    model = CustomerAddress

admin.site.register(CustomerAddress,CustomerAddressAdmin)