import uuid

from django.shortcuts import render, get_object_or_404, redirect

from shop.forms import SearchForm
from shop.models import Items, CartItem

CART_COOKIE_NAME = 'cart_id'
def item_view(request):
    if request.method == 'GET':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_body = form.cleaned_data['search_body']
            return redirect('search', search_body=search_body)
    else:
        form = SearchForm()

    items = Items.objects.all()
    context = {
        'items': items,
        'form': form,
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

    response = redirect('mainpage')

    response.set_cookie(CART_COOKIE_NAME, cart_id, max_age=3600 * 24 * 30)
    return response

def cart_view(request):
    cart_id = request.COOKIES.get(CART_COOKIE_NAME)
    cart_items = CartItem.objects.filter(cart_id=cart_id) if cart_id else []
    total_price = sum(item.get_cost() for item in cart_items)

    if total_price and request.method == 'POST':
        CartItem.objects.filter(cart_id=cart_id).delete()
        return redirect('cart_view')
    for item in cart_items:

        if item.quantity == 0:
            item.delete()
            item.save()
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
def search(request):
    search_body = request.GET.get('search_body', '')
    form = SearchForm()
    search_results = []
    if search_body:
        items = Items.objects.all()
        search_results = [item for item in items if search_body.lower() in item.name.lower()]

    context = {
        'search_results': search_results,
        'search_body': search_body if 'search_body' in request.GET else '',
        'form': form,
    }
    return render(request, 'search.html', context)
def item_card(request, item_id):
    item = get_object_or_404(Items, pk=item_id)
    context = {
        'item': item,
        'item_id': item_id,
    }
    return render(request, 'item.html', context)
def minus(request, item_id):
    item = get_object_or_404(Items, pk=item_id)
    cart_id = request.COOKIES.get(CART_COOKIE_NAME)
    cart_item = CartItem.objects.get(cart_id=cart_id, item=item) if cart_id else []
    if request.method == 'POST':
        if cart_item.quantity > 0:
                cart_item.quantity -= 1
                cart_item.save()
                if cart_item.quantity == 0:
                    cart_item.delete()
                return redirect('cart_view')
    return redirect('cart_view')
def plus(request, item_id):
    item = get_object_or_404(Items, pk=item_id)
    cart_id = request.COOKIES.get(CART_COOKIE_NAME)
    cart_item = CartItem.objects.get(cart_id=cart_id, item=item) if cart_id else []
    if request.method == 'POST':
        if cart_item.quantity > 0:
            cart_item.quantity += 1
            cart_item.save()
            return redirect('cart_view')
    return redirect('cart_view')
