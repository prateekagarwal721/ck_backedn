from rest_framework import serializers, fields
from payment.models import Invoice,InvoiceItem
from utils.number import indian_formatted_currency

class InvoiceItemSerializer(serializers.ModelSerializer):
    amount = serializers.SerializerMethodField()

    def get_amount(self, obj):
        return indian_formatted_currency(obj.amount)
        
        
    class Meta:
        model = InvoiceItem
        fields = ("amount","description","amount_type")



