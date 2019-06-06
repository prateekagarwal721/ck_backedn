from django.contrib import admin
from django_extensions.admin import ForeignKeyAutocompleteAdmin
from ckuser.models import CKUser

# Register your models here.
class CKUserAdmin(ForeignKeyAutocompleteAdmin):
    model = CKUser

admin.site.register(CKUser,CKUserAdmin)