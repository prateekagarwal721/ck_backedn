from rest_framework import serializers, fields
from payment.models import Invoice,InvoiceItem
from decimal import Decimal

class InvoiceItemSerializer(serializers.ModelSerializer):
    amount = serializers.SerializerMethodField()

    def get_amount(self, obj):
        amount = obj.amount
        prefix = ""
        if amount<0:
            prefix = "-"
        amount = abs(int(round(amount)))
        amount, thousands = divmod(amount, 1000)
        if amount > 0:
            thousands = str(int(thousands)).zfill(3)
        groups = [thousands]
        while amount:
            amount, group = divmod(amount, 100)
            if amount > 0:
                group = str(group).zfill(2)
            groups.insert(0, group)
        result = ','.join(map(str, groups))
        return prefix + result
        
    class Meta:
        model = InvoiceItem
        fields = ("amount","description","amount_type")



