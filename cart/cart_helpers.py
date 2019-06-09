from cart.models import Order, Item
from customer.models import Customer
from django.db.models import Sum
from payment.models import Invoice, InvoiceItem
from product.models import Product
from django.contrib.contenttypes.models import ContentType


def update_invoice(order):
    invoice_instance,created = Invoice.objects.get_or_create(
                               customer=order.customer,order=order )
    if created:
        invoice_instance.save()

    for item in order.item_set.all():
        update_invoice_item(item,invoice_instance)

    items_in_order = order.item_set.all().values_list("id",flat=True)   
    total_amount = 0
    for invoice_item in invoice_instance.items.all():
        if invoice_item.cart_item_id in items_in_order:
            total_amount+= invoice_item.amount
        else:
            invoice_item.delete()#Item might have been removed from cart.
    
    order.amount = total_amount
    order.save()            



def update_invoice_item(item,invoice_instance):
    if type(item.object)==Product:
        import json
        import ast
        extra_details = json.loads(json.dumps(ast.literal_eval(item.extra_details)))
        quantity = extra_details['quantity']
        print quantity
        product = item.object
        item.quantity = quantity
        amount = product.price * quantity
        tax = round(product.price * quantity * 0.18)
        description = product.name

        invoiceitem_instance,created = InvoiceItem.objects.get_or_create(invoice=invoice_instance,cart_item=item,amount_type='item_price')
        invoiceitem_instance.amount = amount    
        invoiceitem_instance.description = description
        invoiceitem_instance.save()

        amount_excluding_tax = InvoiceItem.objects.filter(invoice=invoice_instance,cart_item=item).exclude(amount_type='tax').aggregate(Sum('amount'))['amount__sum']
        amount_item_price = InvoiceItem.objects.filter(invoice=invoice_instance,cart_item=item,amount_type='item_price').aggregate(Sum('amount'))['amount__sum']
        print "Amount exluding tax is: "
        print amount_excluding_tax

        item.amount = round(amount_excluding_tax,2)
        item.item_price = round(amount_item_price,2)
        item.save()
        #Add item for tax.
        invoiceitem_tax,created = InvoiceItem.objects.get_or_create(invoice=invoice_instance,cart_item=item,amount_type='tax')
        invoiceitem_tax.amount = round(amount_excluding_tax * 0.18,1)
        invoiceitem_tax.description = 'GST'
        invoiceitem_tax.save()

def add_to_cart(customer,item,extra_details={}):
    current_order = get_current_order(customer,True)
    cart_item,created = Item.objects.get_or_create(order=current_order, object_id=item.id, content_type=ContentType.objects.get_for_model(item))
    cart_item.extra_details = extra_details
    cart_item.save()
    update_invoice(current_order)
    return current_order

def remove_from_cart(customer,item_id):
    current_order = get_current_order(customer,True)
    print "Current order for user %s" %str(customer.user)
    cart_item = Item.objects.get(order=current_order, id=item_id)
    cart_item.delete()
    update_invoice(current_order)
    return current_order

def get_current_order(customer,create_if_needed=False):
    print "Gettting current order for user %s" %str(customer.user)

    current_order = Order.objects.filter(status=1,customer=customer).order_by("created_on").last()
    if not current_order and create_if_needed:
        print "No current order. %s" %str(customer.user)
        current_order = Order(customer=customer)
        current_order.save()
        print "Created order. %s" %str(customer.user)

    return current_order
