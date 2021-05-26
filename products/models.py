from django.db import models

from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from django.db.models.fields import AutoField
# Create your models here.

class Product(models.Model):
    id = AutoField(primary_key=True,auto_created=True)
    product_name = models.CharField(max_length=30,blank=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product_price = models.PositiveIntegerField()
    category = models.CharField(max_length=10)
    product_discription = models.TextField(blank=False )
    image = models.ImageField(upload_to="products")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product_name


class Cart(models.Model):
    """docstring for Cart."""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product , on_delete = models.CASCADE)
    Count = models.PositiveIntegerField()

    class Meta:
        unique_together = ["user", "product_id"]
class Wishlist(models.Model):
    """docstring for Wishlist."""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product , on_delete = models.CASCADE)


class Billing_Adress(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Company_name = models.CharField(blank=True,max_length=30)
    House = models.CharField(max_length=30)
    Adress = models.TextField(blank=True)
    Zip = models.CharField(blank=True, max_length=6)
    Town = models.CharField(max_length=30)
    Phone = models.CharField(max_length=10)
    Email = models.EmailField(max_length=254)
    Additional_Information = models.TextField(blank=True)
    def __str__(self):
        return str(self.First_Name)
