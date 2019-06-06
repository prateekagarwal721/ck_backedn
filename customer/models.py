from django.db import models
from ckuser.models import CKUser
from django.utils.translation import ugettext as _

# Create your models here.
def get_upload_to(instance, filename):
    return 'profile_pic/%s-%s-%f.jpg' % (instance.user.mobile_no,instance.name,time.time())

class Customer(models.Model):
    user = models.ForeignKey(CKUser)

    name = models.CharField(max_length=255,default='',null=True, blank=True)
    profile_pic = models.ImageField(upload_to=get_upload_to, blank=True)

    TYPE_DEFAULT = 0
    TYPE_RETAILER = 1
    TYPE_WHOLESALER = 2
    TYPE_MANUFACTURER = 3
    TYPE_OTHER = 4

    TYPE_OPTIONS = (
        (0, 'Default'),
        (1, 'Retailer'),
        (2, 'Wholesaler'),
        (3, 'Manufacturer'),
        (4, 'Other')
    )
    customer_business_type = models.PositiveIntegerField(choices=TYPE_OPTIONS, null=True, blank=True)
    primary_zip_code = models.CharField(_("zip code"), max_length=6, null=True, blank=True)