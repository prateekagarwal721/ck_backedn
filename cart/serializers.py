from rest_framework import serializers, fields
from ckuser.models import CKUser
from cart.models import Order,Item
from payment.models import Invoice, InvoiceItem
from customer.models import Customer
from product.models import Product
from payment.serializers import InvoiceItemSerializer

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    status = serializers.ReadOnlyField(source='get_state_display')
    summary = serializers.SerializerMethodField()
    amount = serializers.SerializerMethodField()
    success = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ("id","extra_details","amount","status","items","summary","success")

    def get_amount(self, obj):
        return round(obj.amount)
    
    def get_success(self,obj):
        return True

    def get_items(self, obj):
        items = obj.item_set.all()
        return ItemSerializer(items, many=True).data

    def get_summary(self, obj):
        invoice = obj.invoice_set.first()
        return invoice.get_summary()

class ItemSerializer(serializers.ModelSerializer):
    object = serializers.SerializerMethodField()
    invoice_items  = serializers.SerializerMethodField()
    item_total = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = ("id","extra_details","invoice_items","object","quantity","item_total") 

    def get_invoice_items(self, obj):
        invoice_items = obj.invoiceitem_set.all().order_by("-amount")
        ordered = sorted(invoice_items, key=lambda n: ( (n.amount_type=='tax'), -1 * n.amount))
        return InvoiceItemSerializer(ordered, many=True).data

    def get_item_total(self,obj):
        invoice_items = obj.invoiceitem_set.all().order_by("-amount")
        total = 0
        for item in invoice_items:
            total += item.amount
        return total
                             
    def get_object(self, obj):
        object = obj.object
        print type(object)
        object_json = {}
        # object_json["type"] = type(object).__name__
        object_json["name"] = object.name
        object_json["short_name"] = object.short_name
        object_json["picture"] = object.get_pic_url()

        return object_json