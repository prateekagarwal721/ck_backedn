from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from product.models import SubCategory,Product
from product.serializers import SubCategorySerializer,ProductSerializer
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    @list_route()
    def get_subcategory(self,request):
        sub_categories = SubCategory.objects.all()
        serializer = SubCategorySerializer(sub_categories,many=True)
        return Response({"sucess":True,"result":serializer.data})

    @list_route()
    def get_product_details(self,request):
        product_id = request.GET.get('product_id')
        product = Product.objects.filter(id=product_id).first()
        serializer = ProductSerializer(product)
        return Response({"sucess":True,"result":serializer.data})