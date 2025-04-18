import uuid
import ssl
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, CreateView

from shop.forms import SearchForm, RegistrationForm, AddItemForm
from shop.models import Items, CartItem

CART_COOKIE_NAME = "cart_id"


def item_view(request):
    if request.method == "GET":
        form = SearchForm(request.POST)
        if form.is_valid():
            search_body = form.cleaned_data["search_body"]
            return redirect("search", search_body=search_body)
    else:
        form = SearchForm()

    items = Items.objects.all()
    context = {
        "items": items,
        "form": form,
    }
    return render(request, "index.html", context)


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

    response = redirect("shop:mainpage")

    response.set_cookie(CART_COOKIE_NAME, cart_id, max_age=3600 * 24 * 30)
    return response


def cart_view(request):
    cart_id = request.COOKIES.get(CART_COOKIE_NAME)
    cart_items = CartItem.objects.filter(cart_id=cart_id) if cart_id else []
    total_price = sum(item.get_cost() for item in cart_items)

    if total_price and request.method == "POST":
        CartItem.objects.filter(cart_id=cart_id).delete()
        return redirect("shop:cart_view")
    for item in cart_items:

        if item.quantity == 0:
            item.delete()
            item.save()
    context = {"cart_items": cart_items, "total_price": total_price}
    return render(request, "cart/cart.html", context)


def remove_from_cart(request, item_id):
    cart_id = request.COOKIES.get(CART_COOKIE_NAME)

    item = get_object_or_404(Items, pk=item_id)

    if cart_id:
        try:
            cart_item = CartItem.objects.get(cart_id=cart_id, item=item)
            cart_item.delete()
        except CartItem.DoesNotExist:
            pass
    response = redirect("shop:cart_view")
    return response


def search(request):
    search_body = request.GET.get("search_body", "")
    form = SearchForm()
    search_results = []
    if search_body:
        items = Items.objects.all()
        search_results = [
            item for item in items if search_body.lower() in item.name.lower()
        ]

    context = {
        "search_results": search_results,
        "search_body": search_body if "search_body" in request.GET else "",
        "form": form,
    }
    return render(request, "search.html", context)


def item_card(request, item_id):
    item = get_object_or_404(Items, pk=item_id)
    if request.method == "POST":
        item.delete()
        return redirect('shop:mainpage')
    context = {
        "item": item,
        "item_id": item_id,
    }
    return render(request, "item.html", context)


def minus(request, item_id):
    item = get_object_or_404(Items, pk=item_id)
    cart_id = request.COOKIES.get(CART_COOKIE_NAME)
    cart_item = CartItem.objects.get(cart_id=cart_id, item=item) if cart_id else []
    if request.method == "POST":
        if cart_item.quantity > 0:
            cart_item.quantity -= 1
            cart_item.save()
            if cart_item.quantity == 0:
                cart_item.delete()
            return redirect("shop:cart_view")
    return redirect("shop:cart_view")


def plus(request, item_id):
    item = get_object_or_404(Items, pk=item_id)
    cart_id = request.COOKIES.get(CART_COOKIE_NAME)
    cart_item = CartItem.objects.get(cart_id=cart_id, item=item) if cart_id else []
    if request.method == "POST":
        if cart_item.quantity > 0:
            cart_item.quantity += 1
            cart_item.save()
            return redirect("shop:cart_view")
    return redirect("shop:cart_view")


def contacts(request):
    return render(request, "contacts.html")


@login_required
def profile(request):
    return render(request, "profile.html")


class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("shop:profile")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@login_required
def email_send_test(request):

    send_mail('pisun', 'hello its just test', 'noreply@nikita-cmo.store', ['atopolev2910@gmail.com'])
    return redirect("shop:mainpage")

@user_passes_test(lambda u: u.is_staff, login_url='shop:error404')
def add_item(request):
    if request.method == "POST":
        form = AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("shop:mainpage")
        else:
            return render(request, 'upload.html', {"form": form})
    else:
        form = AddItemForm()
    return render(request, 'upload.html', {"form": form})

def error404(request):
    return render(request, "404.html")