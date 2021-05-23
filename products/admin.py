from django.contrib import admin

from .models import Product,Cart,Wishlist,Shipping_Adress
# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Shipping_Adress)
