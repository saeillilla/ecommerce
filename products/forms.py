from django import forms
from .models import Product
class createProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','product_discription','category','product_price',  'image']
