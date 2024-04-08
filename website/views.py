from .models import Product,  Order, Category
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

"""
Loads the product page of the website
"""
def index(request):
    cartDict = request.session.get('cart')
    if not cartDict:
        request.session['cart'] = {}
    all_categories = Category.objects.all()
    cat_id = request.GET.get('categorie')
    if cat_id:
        if cat_id == "10":
            products = Product.objects.all()
        else:
            products = Product.fetch_products_by_category(cat_id)
    else:
        products = Product.objects.all()
    all_data = {}
    all_data['products'] = products
    all_data['categories'] = all_categories
    product_id = request.POST.get('product')
    is_remove = request.POST.get('remove')
    if product_id is not None:
        cartDict = request.session.get('cart')
        if cartDict:
            quantity = cartDict.get(product_id)
            if quantity:
                if is_remove:
                    if quantity <= 1:
                        cartDict.pop(product_id)
                    else:
                        cartDict[product_id] = quantity - 1
                else:
                    cartDict[product_id] = quantity + 1
            else:
                cartDict[product_id] = 1
        else:
            cartDict = {}
            cartDict[product_id] = 1
        request.session['cart'] = cartDict
        total_price = 0
        if request.session['cart']:
            for id in request.session['cart']:
                qty = request.session['cart'][id]
                p = Product.objects.get(id=id)
                total_price += p.price * qty
        request.session['final_price'] = total_price
    return render(request, 'index.html', all_data)

"""
This function loads the cart page of the website
"""
def cart(request):
    if request.method == 'POST':
        id_list = list(request.session.get('cart').keys())
        product_list = Product.fetch_products(id_list)
        return render(request, 'cart.html', {'products': product_list })
    else:
        id_list = list(request.session.get('cart').keys())
        product_list = Product.fetch_products(id_list)
        return render(request, 'cart.html', {'products': product_list})


""" This function loads the shipping page"""
def shipping(request):
    return render(request, 'shipping.html')

""" This function loads the summary page"""
def summary(request):
    return render(request, 'Summary.html')

""" This function loads the payment page"""
def payment(request):
    request.session['address'] = request.POST.get("address")
    request.session['phone'] = request.POST.get("phone")
    #we add the shipping cost here by default 20
    request.session['delivery_price'] = request.session.get("final_price") + 20
    return render(request, 'payment.html')

""" This function loads the Confirmation page"""
def confirm(request):
    address = request.session.get('address')
    mobile = request.session.get('phone')
    user_id = request.session.get('user_id')
    cart_items = request.session.get('cart')
    product_list = Product.fetch_products(list(cart_items.keys()))
    for prod in product_list:
        order = Order(user=User(id=user_id), product=prod, price=prod.price, quantity=cart_items.get(str(prod.id)), address=address, phone=mobile)
        order.confirm_order()
    request.session['cart'] = {}
    return render(request, 'confirm.html')

