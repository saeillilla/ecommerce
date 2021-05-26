from django.shortcuts import render,redirect,HttpResponse
from .models import Product,Cart,Wishlist,Billing_Adress
from django.contrib.auth.decorators import login_required
from .forms import createProduct 
import razorpay
from django.views.decorators.csrf import csrf_exempt
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
    return render(request, 'products/productdetails.html',{'product':obj,'flag':flag})

@login_required
def addCart(request , data):
    u = data.split('_')
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


def removeFromWishlist1(request,id):
    product = Product.objects.get( id= id)
    list = Wishlist.objects.filter(user = request.user)
    for i in list:
        if i.product_id == product:
            i.delete()
    return redirect('/products/wishlist/')


def view_wishlist(request):
    details =[]
    flag = 'true'
    obj = Wishlist.objects.filter(user = request.user)
    for i in obj:
        product = Product.objects.get(product_name = i.product_id)
        s = {'id':product.id,'name':product.product_name, 'image':product.image , 'product_discription':product.product_discription }
        details.append(s)
    if len(obj)==0:
        flag = "false"
    return render(request,'products/wishlist.html',{'products':details,'flag':flag})

def myProducts(request):
    product = Product.objects.filter(user = request.user)

    return render(request,'products/user_products.html',{'context':product})
def checkout(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        companyName = request.POST['companyName']
        house = request.POST['house']
        adress = request.POST['adress']
        zipcode = request.POST['zipcode']
        town = request.POST['town']
        phone = request.POST['phone']
        email = request.POST['email11']
        additionalinformation = request.POST['additionalinformation']
        obj = Billing_Adress(user = request.user , First_Name =firstName,Last_name = lastName , Company_name = companyName , House = house, Adress = adress,Zip=zipcode,Town =town,Phone =phone,Email = email, Additional_Information =additionalinformation   )
        obj.save()
        return redirect('/')
    obj = Billing_Adress.objects.filter(user = request.user)
    
    if len(obj)==1:
        return redirect('/products/payment/')
        
    else:
        print('hello')
        obj1 = Cart.objects.filter(user = request.user)
        sum = 0
        for i in obj1:
            x = Product.objects.get(product_name = i.product_id)
            temp = int(x.product_price)*int(i.Count)
            sum +=temp
        return render(request,'products/checkout.html',{'sum':sum})


def payment1(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000

        client = razorpay.Client(
            auth=("rzp_test_vB5NPppo2BB5Mt", "BVrzePf4vi4PHRAPQFV2QU3x"))

        payment = client.order.create({'amount': amount, 'currency': 'INR','payment_capture': '1'})
    obj = Billing_Adress.objects.filter(user = request.user)
    obj1 = Cart.objects.filter(user = request.user)
    sum = 0
    for i in obj1:
        x = Product.objects.get(product_name = i.product_id)
        temp = int(x.product_price)*int(i.Count)
        sum +=temp
    return render(request, 'products/checkout1.html',{'details':obj[0],'price':sum})

@csrf_exempt
def success(request):
    return render(request, "success.html")