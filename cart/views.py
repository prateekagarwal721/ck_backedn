from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from cart.models import Order,Item
from ckuser.serializers import CKUserSerializer
from rest_framework.decorators import list_route, detail_route
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from product.models import Product
from customer.models import Customer
from cart.cart_helpers import add_to_cart,remove_from_cart,get_current_order,update_invoice
from cart.serializers import OrderSerializer

# Create your views here.
class CartViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = CKUserSerializer

    @list_route(methods=['post'])
    def add_to_cart(self,request):
        product_id = request.data.get('product_id')
        print 'product_id'
        print product_id
        extra_details = request.data.get('extra_details')
        print extra_details
        item_to_add = Product.objects.get(pk=product_id)
        customer = Customer.objects.get(id=request.data.get('customer_id'))
        print customer
        current_order = add_to_cart(customer, item_to_add, extra_details)

        serializer = OrderSerializer(current_order)
        return Response({"success":True,"result":serializer.data})

    @list_route(methods=['post'])
    @csrf_exempt
    def remove_from_cart(self, request):
        print "remove_from_cart api"
        # customer = UserHelper.get_customer(request.user,request)
        customer = Customer.objects.get(id=request.data.get('customer_id'))     
        item_id = request.data.get('item_id')
        current_order = remove_from_cart(customer, item_id)
        serializer = OrderSerializer(current_order)
        return Response({"success":True,"result":serializer.data})

    @list_route(methods=['get'])
    @csrf_exempt
    def view(self, request):
        print "view api"
        user = request.user
        # if not user.is_authenticated():
        #     return HttpResponse('Unauthorized', status=401)
        # customer = UserHelper.get_customer(request.user,request)
        customer = Customer.objects.get(id=request.GET.get('customer_id')) 
        current_order = get_current_order(customer)
        if current_order:  
            update_invoice(current_order)
        serializer = OrderSerializer(current_order)
        return Response({"success":True,"result":serializer.data})