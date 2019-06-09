from ckuser.models import CKUser
from customer.models import Customer


class UserHelper(object):

    @classmethod
    def get_customer(cls, user, request=None):
        customer = None
        if request and ('customer_id' in request.session):
            customer_id = request.session['customer_id']
            customer = Customer.objects.filter(id=customer_id,user=user).first()

        if not customer and user.is_authenticated():
            customer = Customer.objects.filter(user=user).first()

        return customer                    
