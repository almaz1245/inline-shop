from django.shortcuts import render
from main.models import Nike,Category,Image
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    nike = Nike.objects.all()
    context = {'nike':nike}
    return render(request, 'index.html',context)

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


def cart(req, id):
    cart_products = req.session.get('cart_products', [])
    cart_products.append(id)
    st = set(cart_products)
    req.session['cart_products'] = list(st)
    nike = Nike.objects.all()
    context = {'Nike':nike}
    print(st)
    return HttpResponseRedirect('/')
def delete(req,id):
    cart_products = req.session.get('cart_products',[])
    cart_products.remove(id)
    req.session['cart_products'] = cart_products
    return HttpResponseRedirect('/')


def cart_page(req):
    cart_product = req.session.get('cart_products', [])
    cart_products = Nike.objects.filter(id__in = cart_product)
    context = {'product':cart_products}
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