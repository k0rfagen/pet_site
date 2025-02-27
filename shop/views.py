import uuid
from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Items, CartItem
from django.views.generic.base import View

CART_COOKIE_NAME = 'cart_id'
def item_view(request):
    items = Items.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)
def add_to_cart(request, item_id):
    item = get_object_or_404(Items, pk=item_id)

    cart_id = request.COOKIES.get(CART_COOKIE_NAME)

    if not cart_id:
        cart_id = str(uuid.uuid4())

    try:
        cart_item = CartItem.objects.get(cart_id=cart_id, item=item)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        CartItem.objects.create(cart_id=cart_id, item=item, quantity=1)

    response = redirect('cart_view')

    response.set_cookie(CART_COOKIE_NAME, cart_id, max_age=3600 * 24 * 30)
    return response

def cart_view(request):
    cart_id = request.COOKIES.get(CART_COOKIE_NAME)
    cart_items = CartItem.objects.filter(cart_id=cart_id) if cart_id else []
    total_price = sum(item.get_cost() for item in cart_items)
    context = {'cart_items': cart_items,
               'total_price': total_price}
    return render(request, 'cart/cart.html', context)

def remove_from_cart(request, item_id):
    cart_id = request.COOKIES.get(CART_COOKIE_NAME)

    item = get_object_or_404(Items, pk=item_id)

    if cart_id:
        try:
            cart_item = CartItem.objects.get(cart_id=cart_id, item=item)
            cart_item.delete()
        except CartItem.DoesNotExist:
            pass
    response = redirect('cart_view')
    return response
def search(request, search_body):
    items = Items.objects.all()
    search_results = []
    for item in items:
        if search_body.lower() in item.name.lower():
            search_results.append(item)
    context = {
        'search_results': search_results,
        'search_body': search_body
    }
    return render(request, 'search.html', context)


