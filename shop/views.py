from django.shortcuts import render
from django.http import HttpResponse
from . models import Product, Contact, Order
from math import ceil
from decimal import Decimal
import json


# Create your views here.
def index(request):
    products= Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    # params = {'no_of_slides':nSlides,'range':range(1,nSlides),'product': products}
    # allProds =[[products, range(1,nSlides), len(products)],[
    # products, range(1,nSlides), len(products)]]
    allProds =[]
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n= len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds': allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method == "POST":
        name =request.POST.get('name', '')
        email=request.POST.get('email', '')
        subject=request.POST.get('subject', '')
        desc=request.POST.get('desc', '')
        print(name, email, subject, desc)
        contact = Contact(name= name , email= email, subject=subject, desc= desc)
        contact.save()


    return render(request, 'shop/contactus.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid ):
    prod = Product.objects.filter(id = myid)
    print(prod)
    return render(request, 'shop/prodview.html', {'product':prod[0]})


def checkout(request):
    products = Product.objects.all()
    products_map = {f"pr{p.id}": {"id": p.id, "name": p.product_name, "price": str(p.price)} for p in products}

    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phonenumber = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        cart_json_str = request.POST.get('cartJson', '{}')

        # Parse JSON and extract total_price
        cart_data = json.loads(cart_json_str)
        items = cart_data.get('items', [])
        total_price = cart_data.get('total_price', 0)

        # Save order
        order = Order(
            name=name,
            email=email,
            phonenumber=phonenumber,
            address=address,
            cart_json=json.dumps(items),  # only save items with names, qty, price
            total_price=total_price
        )
        order.save()

    context = {"products_map_json": json.dumps(products_map)}
    return render(request, "shop/checkout.html", context)