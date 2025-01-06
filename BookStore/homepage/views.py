from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Booksupload, wishlist, BookReview, cart, Cartitem
from .forms import UploadForm


def Home(request):
    Book = Booksupload.objects.all()
    context = {'books_t': Book}
    return render(request, 'home.html', context)

def About(request):
    return render(request, 'about.html')


# from here login required to excess the page

from django.contrib.auth.decorators import login_required    

@login_required(login_url = 'login')
def Upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UploadForm()
    return render(request, 'Bookupload.html', {'form': form})


# login, signup, logout

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = user_name, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'form': form})
        else:
            form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')


def show_product(request, id):
    product = get_object_or_404(Booksupload, id=id)
    # For Review
    review = BookReview.objects.filter(product = product)
    return render(request, 'product.html', {"product": product, "reviews": review})

def addtowish(request, id):
    user = request.user
    product = Booksupload.objects.get(id=id)
    obj1, created = wishlist.objects.get_or_create(user=user)
    obj1.products.add(product)
    obj1.save()
    return redirect('home')

def show_wishlist(request):
    user = request.user
    wish_object = wishlist.objects.get(user=user)
    return render(request, 'wishlist.html', {"user_products": wish_object.products.all()})

def removewish(request, id):
    product_rm = Booksupload.objects.get(id=id)
    wish_obj = wishlist.objects.get(user = request.user)
    wish_obj.products.remove(product_rm)
    return redirect('show_wishlist')
    
    # return render(request, 'wishlist.html', {"user_product": wish_obj.products.all()})


# def addtocart(request, id):
#     user = request.user
#     product = Booksupload.objects.get(id=id)
#     obj1, created = cart.objects.get_or_create(user=user)
#     obj1.products.add(product)
#     obj1.save()
#     return redirect('home')


def addtocart(request, id):
    user_cart, created = cart.objects.get_or_create(user = request.user)
    product = Booksupload.objects.get(id=id)
    cart_item, created = Cartitem.objects.get_or_create(product = product, user = user_cart)
    cart_item.product = product
    cart_item.save()
    return redirect('home')


# def show_cart(request):
#     user = request.user
#     cart_object = cart.objects.get(user=user)
#     return render(request, 'cart.html', {"user_products": cart_object.products.all()})


def show_cart(request):
    user_cart, created = cart.objects.get_or_create(user = request.user)
    cart_object = user_cart.cartitem_set.all()
    return render(request, 'cart.html', {"user_products": cart_object})


# def removecart(request, id):
#     product_rm = Booksupload.objects.get(id=id)
#     cart_obj = cart.objects.get(user = request.user)
#     cart_obj.products.remove(product_rm)
# return render(request, 'cart.html', {"user_products": cart_obj.products.all()})


def removecart(request, id):
    product_rme = Cartitem.objects.get(pk=id)  
    product_rme.delete()
    return redirect('show_cart')

