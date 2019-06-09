from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category,null=True,blank=True) 
    picture = models.ImageField(blank=True, upload_to="product")
    picture_extra_1 = models.ImageField(blank=True, upload_to="product")
    picture_extra_2 = models.ImageField(blank=True, upload_to="product")
    picture_extra_3 = models.ImageField(blank=True, upload_to="product")
    specification = models.TextField(null=True,blank=True)

    def __unicode__(self):
        return self.name

    def get_pic_url(self):
        return self.picture.url

class Product(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255, null=True, blank=True, default="")
    sub_category = models.ForeignKey(SubCategory,null=True,blank=True)
    specification = models.TextField(null=True,blank=True)
    price = models.FloatField(default=0)
    product_code = models.SlugField(max_length=6, unique=True, null=True, blank=True)
    picture = models.ImageField(blank=True, upload_to="product")
    picture_extra_1 = models.ImageField(blank=True, upload_to="product")
    picture_extra_2 = models.ImageField(blank=True, upload_to="product")
    picture_extra_3 = models.ImageField(blank=True, upload_to="product")
    is_available = models.BooleanField(default=True)

    class Meta:
        unique_together = ('sub_category','product_code')

    def __unicode__(self):
        return self.name

    def get_pic_url(self):
        if self.picture:
            return self.picture.url
        return


    