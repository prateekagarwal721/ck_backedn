from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.db.models.signals import post_save


# Create your models here.

class CKUserManager(BaseUserManager):

    @classmethod
    def normalize_email(cls, email):
        COMMON_EMAILS = set(['gmail', 'yahoo', 'hotmail', 'live', 'aol', 'outlook', 'facebook'])

        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            domain_part = domain_part or ''
            try:
                domain_name = domain_part.split('.', 1)[0]
            except (ValueError, IndexError):
                pass
            else:
                if domain_name.lower() in COMMON_EMAILS:
                    email_name = email_name.lower()

            email = '@'.join([email_name, domain_part.lower()])

        return email

    @classmethod
    def normalize_mobile_no(cls, mobile_no):
        mobile_no = mobile_no.lstrip("0")
        if mobile_no.startswith("+91"):
            mobile_no = mobile_no[3:]
        return mobile_no

    def _create_user(self, mobile_no, password, is_staff, is_superuser, **extra_fields):
        
        email = extra_fields.pop('email', None)
        if email:
            email = self.normalize_email(email)
        
        mobile_no = self.normalize_mobile_no(mobile_no)
        now = timezone.now()

        user = self.model(email=email,mobile_no=mobile_no,
                            is_staff=is_staff, is_active=True,
                            is_superuser=is_superuser, last_login=now,
                            date_joined=now, **extra_fields
                            )
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        
        user.save(using=self._db)
        return user



    def create_user(self, mobile_no, password=None, **extra_fields):
        return self._create_user(mobile_no,password, False, False, **extra_fields)

    def create_superuser(self, mobile_no, password, **extra_fields):
        return self._create_user(mobile_no,password,True,True,**extra_fields)

    def get_by_natural_key(self,mobile_no):
        mobile_no = self.normalize_mobile_no(mobile_no)
        return BaseUserManager.get_by_natural_key(self, mobile_no)

class CKUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "mobile_no"
    REQUIRED_FIELDS = ["name"]

    name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now())

    objects = CKUserManager()

    def firstname(self):
        return self.name.split()[0]

    def get_short_name(self):
        return self.firstname

def create_a_customer_for_every_user(instance, created, **kwargs):
    if created:
        from customer.models import Customer
        if not Customer.objects.filter(user=instance).exists():
            Customer.objects.create(user=instance, name=instance.name)

post_save.connect(create_a_customer_for_every_user, sender=CKUser)