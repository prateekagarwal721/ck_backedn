from django.db import models
from customer.models import Customer
from django.utils.translation import ugettext as _
# Create your models here.

class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer)
    address_1 = models.CharField(_("address"), max_length=128, blank=True, null=True)
    address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True, null=True)
    city = models.CharField(_("city"), max_length=64, null=True, blank=True)
    state = models.CharField(_("state"),max_length=64, null=True, blank=True)
    zip_code = models.CharField(_("zip code"), max_length=6)
    description = models.TextField(null=True, blank=True)
