from django.db.models import Sum
from rest_framework import serializers, fields

from product.models import Product, Category, SubCategory

class SubCategorySerializer(serializers.ModelSerializer):
    products = fields.SerializerMethodField()
    picture = fields.SerializerMethodField()

    class Meta:
        model = SubCategory
        fields = ("id","name","specification","category","products","picture")

    def get_products(self,obj):
        products = Product.objects.filter(sub_category=obj)[:5]
        return ProductSerializer(products,many=True).data

    def get_picture(self,obj):
        print obj.picture.url
        return obj.picture.url
        

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
