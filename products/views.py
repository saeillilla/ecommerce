from django.shortcuts import render,redirect
from .models import Product,Cart,Wishlist,Shipping_Adress
from django.contrib.auth.decorators import login_required
from .forms import createProduct
# Create your views here.

@login_required
def addProduct(request):
    if request.method == 'POST':
        form = createProduct(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/')
    form = createProduct()
    return render(request,'products/addproduct.html',{'form':form})

def all_products(request):
    obj = Product.objects.all()
    return render(request, 'products/viewproducts.html',{'products':obj})

def view_products(request , id):
    obj = Product.objects.get(id = id)
    list = Wishlist.objects.filter(product_id = obj)
    flag = 'false'
    for i in list:
        if i.user == request.user:
            flag = 'true'
    print(flag)
    return render(request, 'products/productdetails.html',{'product':obj,'flag':flag})

@login_required
def addCart(request , data):
    u = data.split('_')
    print(u)
    product = Product.objects.get(id = int(u[0]))
    obj = Cart(user = request.user , product_id = product , Count = int(u[1]))
    obj.save()
    return redirect('/')
@login_required
def cart(request):
    details =[]
    obj = Cart.objects.filter(user = request.user)
    for i in obj:
        product = Product.objects.get(product_name = i.product_id)
        s = {'id':product.id,'name':product.product_name, 'image':product.image , 'product_discription':product.product_discription , 'count':i.Count}
        details.append(s)

    print(details)
    return render(request, 'products/cart.html',{'details':details})

def removeFromCart(request,id):
    product = Product.objects.get( id= id)
    obj = Cart.objects.filter(product_id = product)
    for i in obj:
        if i.user == request.user:
            i.delete()
    return redirect('/products/cart/')

def addWishlist(request,id):
    product = Product.objects.get( id= id)
    list = Wishlist.objects.all()
    flag = 1
    for i in list:
        if i.product_id == product:
            flag = 0
    if flag == 1:
        obj = Wishlist(product_id =product, user=request.user )
        obj.save()
    url = '/products/viewproduct/'+str(id)+'/'
    return redirect(url)


def removeFromWishlist(request,id):
    product = Product.objects.get( id= id)
    list = Wishlist.objects.filter(user = request.user)
    for i in list:
        if i.product_id == product:
            i.delete()
    url = '/products/viewproduct/'+str(id)+'/'
    return redirect(url)
