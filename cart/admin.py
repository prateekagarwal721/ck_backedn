from django.contrib import admin
from django_extensions.admin import ForeignKeyAutocompleteAdmin
from cart.models import Order,Item

# Register your models here.
class OrderAdmin(ForeignKeyAutocompleteAdmin):
    model = Order

class ItemAdmin(ForeignKeyAutocompleteAdmin):
    model = Item


admin.site.register(Order,OrderAdmin)
admin.site.register(Item,ItemAdmin)