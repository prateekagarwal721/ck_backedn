from django.db import models
from customer.models import Customer
from cart.models import Order, Item
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from utils.number import indian_formatted_currency

# Create your models here.
class Invoice(models.Model):
    description = models.TextField(blank=True, default='')
    customer = models.ForeignKey(Customer)
    order = models.ForeignKey(Order, null=True, unique=True)

    def get_summary(self):
        invoice = self
        item_total = 0
        order_total = 0
        unique_labels = []
        adjustments = {}
        price_summary = []        
        if invoice:
            for item in invoice.items.all():
                order_total += item.amount
                if item.amount_type == "item_price":
                    item_total += item.amount
                else:
                    if item.description in unique_labels:
                        adjustments[item.description] += item.amount
                    else:
                       unique_labels.append(item.description)
                       adjustments[item.description] = item.amount     
            price_summary = []
            price_summary.append({'label':'Item total','value':indian_formatted_currency(round(item_total))})
            for key,value in adjustments.items():
                price_summary.append({'label':key,'value':indian_formatted_currency(round(value))})
            price_summary.append({'label':'Order total','value':indian_formatted_currency(round(order_total))})
        return price_summary


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name="items")
    cart_item = models.ForeignKey(Item, null=True)
    amount = models.FloatField(default=0, help_text="In case of custom items, say a T shirt for 500")
    pro_rata_factor = models.FloatField(default=1)

    description = models.CharField(max_length=200, blank=True, default='')
    amount_type = models.CharField(max_length=100, null=True,default='item_price')# item_price, tax, shipping_charge etc

    is_eligible = models.BooleanField(default=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,null=True,blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    source = GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together = ('invoice', 'cart_item','amount_type')    