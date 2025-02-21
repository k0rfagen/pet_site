import uuid
from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Items, CartItem
from django.views.generic.base import View

CART_COOKIE_NAME = 'cart_id'
class ItemView(View):
    def get(self, request):
        items = Items.objects.all()
        context = {
            'items': items
        }
        return render(request, 'index.html', context)
class AddToCartView(View):
    def post(self, request, item_id):
        item = get_object_or_404(Items, pk=item_id)

        cart_id = request.COOKIES.get(CART_COOKIE_NAME)

        if not cart_id:
            cart_id = str(uuid.uuid4())  # Генерируем UUID и преобразуем его в строку

        try:
            cart_item = CartItem.objects.get(cart_id=cart_id, item=item)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            CartItem.objects.create(cart_id=cart_id, item=item, quantity=1)

        response = redirect('cart_view')

        # 8. Устанавливаем куки с ID корзины
        response.set_cookie(CART_COOKIE_NAME, cart_id, max_age=3600 * 24 * 30)  # 30 дней
        return response

class CartView(View):
    def get(self, request):
        cart_id = request.COOKIES.get(CART_COOKIE_NAME)
        cart_items = CartItem.objects.filter(cart_id=cart_id) if cart_id else []
        total_price = sum(item.get_cost() for item in cart_items)
        context = {'cart_items': cart_items,
                   'total_price': total_price}
        return render(request, 'cart/cart.html', context)

class RemoveFromCartView(View):
    def post(self, request, item_id):
        cart_id = request.COOKIES.get(CART_COOKIE_NAME)

        item = get_object_or_404(Items, pk=item_id)

        if cart_id:
            try:
                cart_item = CartItem.objects.get(cart_id=cart_id, item=item)
                cart_item.delete()
            except CartItem.DoesNotExist:
                pass  # Если CartItem не найден, ничего не делаем

        response = redirect('cart_view')
        return response