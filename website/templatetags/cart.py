from django import template
register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False




"""Function used to filter the items by count"""
@register.filter(name='count')
def get_count(productObj, cartObj):
    items = cartObj.keys()
    for id in items:
        if int(id) == productObj.id:
            return cartObj.get(id)
    return 0

"""Funciton used to get the sub total"""
@register.filter(name='price_total')
def get_sub_total(product, cart):
    return product.price * get_count(product, cart)


"""Function used to get he total price """
@register.filter(name='total_cart')
def final_total(products, cart):
    res = 0
    for p in products:
        res += get_sub_total(p, cart)
    return res


@register.filter(name='total_100')
def total_100(products, cart):
    ans = 100 + final_total(products, cart)
    return ans


@register.filter(name='coupon')
def coupon(offers, codes):
    c = 0
    for offer in offers:
        if codes in offer.code:
            if codes != "":
                c += 1
    if c == 0:
        return False
    else:
        return True


@register.filter(name='ctotal')
def ctotal(ptotal, dvalue):
    return ptotal - (ptotal * dvalue) / 100
