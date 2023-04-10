from django.shortcuts import render
from main.models import Nike,Category,Image, Order, OrderItem
from django.http import HttpResponseRedirect
import uuid 
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    nike = Nike.objects.all()
    context = {'nike':nike}
    return render(request, 'index.html',context)


@login_required(login_url='/sign_up/')
def remove_form(req,id):
    favorites_products = req.session.get('favorites_products',[])
    favorites_products.remove(id)
    req.session['favorites_products'] = favorites_products
    return HttpResponseRedirect('/')


def detail(req,id):
    product = Nike.objects.get(id=id)
    images = Image.objects.filter(sneakers=product)
    return render(req,'detail.html',{'product':product,'images':images})


def favorites(req,id):
    favorites_products = req.session.get('favorites_products',[])
    favorites_products.append(id)
    # favorites_products.remove(id)
    st = set(favorites_products)
    req.session['favorites_products'] = list(st)
    nike = Nike.objects.all()
    context = {'nike':nike}
    print(st)
    return render(req,'index.html',context)



@login_required(login_url='/sign_up/')
def cart(req, id):
    cart_products = req.session.get('cart_products', [])
    cart_products.append(id)
    st = set(cart_products)
    req.session['cart_products'] = list(st)
    nike = Nike.objects.all()
    return HttpResponseRedirect('/')

def delete(req,id):
    cart_products = req.session.get('cart_products',[])
    cart_products.remove(id)
    req.session['cart_products'] = cart_products
    return HttpResponseRedirect('/')

@login_required(login_url='/sign_up/')
def cart_page(req):
    cart_product = req.session.get('cart_products', [])
    cart_products = Nike.objects.filter(id__in = cart_product)
    total_price = 0
    for i in cart_products:
        total_price += i.price
    context = {'product':cart_products,'amount':cart_products.count(), 'total_price':total_price}
    return render(req, 'card.html', context)




def remove_from_cartpage(req,id):
    cart_products = req.session.get('cart_products', [])
    cart_products.remove(id)
    req.session['cart_products'] = cart_products
    return HttpResponseRedirect('/')


def favorites_page(req):
    favorites_products = req.session.get('favorites_products', []) 
    favorites_products = Nike.objects.filter(id__in = favorites_products) 
    return render(req,'favorite.html',{'nike':favorites_products})

def abaut(req):
    return render(req,'abaut.html')

@login_required(login_url='/sign_up/')
def order(request):
    if request.method == 'POST':
        cart_product = request.session.get('cart_products', [])
        cart_products = Nike.objects.filter(id__in = cart_product)
        total_price = 0
        for i in cart_products:
            total_price += i.price
        order = Order.objects.create(
        user = request.user,
        total_price = total_price,
        address = request.POST.get('address'),
        code = uuid.uuid4(),
        phone_number = request.POST.get('phone_number'),
        message = request.POST.get('message'),
        )
        for i in cart_products:
            item = OrderItem.objects.create(
                order=order,
                product=i,
            )
    cart_products = request.session.get('cart_products',[])
    cart_products = []
    request.session['cart_products'] = cart_products
    return render(request,'order.html')
