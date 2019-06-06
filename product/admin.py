from django.contrib import admin
from django_extensions.admin import ForeignKeyAutocompleteAdmin
from product.models import Category, SubCategory, Product

# Register your models here.
class CategoryAdmin(ForeignKeyAutocompleteAdmin):
    model = Category

class SubCategoryAdmin(ForeignKeyAutocompleteAdmin):
    model = SubCategory

class ProductAdmin(ForeignKeyAutocompleteAdmin):
    model = Product

admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Product,ProductAdmin)