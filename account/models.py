from django.db import models
#   from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    wishlist = models.BooleanField(default=False)
    cartlist = models.BooleanField(default=False)
    old_price = models.FloatField(max_length=200, null=True, blank=True)
    new_price = models.FloatField(max_length=200, null=True, blank=True)
    discount = models.CharField(max_length=2, null=True, blank=True)

    refund = models.BooleanField(default=True) 
    in_stock = models.BooleanField(default=True)
    seller_name = models.CharField(max_length=200, null=True, blank=True)
    features = models.TextField(max_length=400, null=True, blank=True)
    specifications = models.TextField(max_length=300, null=True, blank=True)

    time_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name[0:50]


class Customer(models.Model):
    #   user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, unique=True, null=True, blank=True)
    profile_pic = models.ImageField(default=None, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name