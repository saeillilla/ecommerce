from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from products.models import Product
# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'sign_up.html',{'form':form})
    form = UserCreationForm()
    return render(request, 'sign_up.html',{'form':form})

def sign_in(request):
    if request.method =='POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user:
                print(user)
                login(request,user)
                return redirect('/')
            else:
                return render(request, 'signin.html',{'error':'Cant sign in.Check username and password'})

    return render(request, 'signin.html',{'error':''})


@login_required
def user_logout(request):
    if(str(request.user) == "AnonymousUser"):
        s=False
    else:
        logout(request)
    return render(request,'home.html')

def home(request):
    if request.method == 'POST':
        obj = Product.objects.filter(product_name = request.POST['searchstring'])
        return render(request,'products/results.html',{'products':obj})
    print(request.user)
    return render(request, 'home.html')
