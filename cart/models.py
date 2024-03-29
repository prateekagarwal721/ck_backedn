from django.db import models
from customer.models import Customer
from address.models import CustomerAddress
from product.models import Product
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(Customer)
    customer_address = models.ForeignKey(CustomerAddress,null=True,blank=True)
    amount = models.FloatField(default=0)
    extra_details = models.TextField(blank=True)

    STATUS_CART = 1
    STATUS_PAYMENT_INITIATED = 2
    STATUS_PAID = 3
    STATUS_SHIPPED = 4
    STATUS_COMPLETED = 5
    STATUS_CANCELLED = 6 

    STATUS_OPTIONS = (
        (1, 'cart'),
        (2, 'payment_initiated'),
        (3, 'paid'),
        (4, 'shipped'),
        (5, 'completed'),
        (6, 'cancelled')
    )
    created_on = models.DateTimeField(default=timezone.now(),blank=True, editable=False)
    status = models.PositiveIntegerField(choices=STATUS_OPTIONS, default=1)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    order = models.ForeignKey(Order) 
    amount = models.FloatField(default=0)
    item_price = models.FloatField(default=0)
    content_type = models.ForeignKey(ContentType,default=12)
    object_id = models.PositiveIntegerField(null=True)
    object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)
    extra_details = models.TextField(null=True, blank=True)