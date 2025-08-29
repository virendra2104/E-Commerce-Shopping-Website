

# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse



from .models import Product, Category






    
# views.py
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})
def rahul(request):
    Product = get_object_or_404(Product, id=id)
    return render(request, 'rahul.html', {'product': Product})

def cart(request):
    return render(request,"cart.html")

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def category(request):
    return render(request,"category.html")
def productdetail(request):
    return render(request,"productdetail.html")

def contact(request):
    return render(request,"contact.html")
def home(request):
    return render(request,"home.html")
def account(request):
    return render(request,"account.html")
def rahul(request):

    return render(request, 'rahul.html')
def men_wear(request):
    products=Product.get_all_products();
    return render(request,'men_wear.html',{'products':products})



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Account created successfully')
            return redirect('signin')
    return render(request,"register.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your homepage URL name
        else:
            return render(request, 'signin.html', {'error': 'Invalid username or password'})
    return render(request, 'signin.html')




def logout_view(request):
    logout(request)
    return redirect('signin')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {'error': 'Invalid username or password'})
    return render(request, 'signin.html')




from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem
from django.db.models import F

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem
from django.db.models import F


from django.shortcuts import redirect, get_object_or_404
from .models import Product, Cart, CartItem



# views.py
from django.shortcuts import redirect, get_object_or_404
from .models import Product, Cart, CartItem

def add_to_cart(request, product_id):
    # Ensure this view is only accessed via POST request
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        quantity = int(request.POST.get('quantity', 1))

        # Handle cart for authenticated vs. anonymous users
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
        else:
            if not request.session.session_key:
                request.session.create()
            cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)

        # Get or create the cart item
        cart_item, item_created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )

        # If the item already exists, just update the quantity
        if not item_created:
            cart_item.quantity += quantity
            cart_item.save()

        return redirect('cart')

    # If the request is not a POST, redirect back to the product page
    return redirect('product_detail', pk=product_id)


from django.shortcuts import render
from .models import Cart, CartItem


def cart_view(request):
    cart = None
    if not request.session.session_key:
     request.session.create()

    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key
        cart = Cart.objects.filter(session_key=session_key).first()

    cart_items = CartItem.objects.filter(cart=cart) if cart else []
    print(f"Cart items retrieved: {cart_items}")

    subtotal = sum(item.get_total_price() for item in cart_items)
    shipping = 4.99
    tax = subtotal * 0.10
    total = subtotal + shipping + tax

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping': shipping,
        'tax': tax,
        'total': total,
    }

    return render(request, 'cart.html', context)


# In views.py, inside the cart_view function
