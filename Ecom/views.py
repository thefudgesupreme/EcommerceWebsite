from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView, TemplateView, View


def home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "homePage.html", context)


def checkout(request):
    return render(request, 'checkoutPage.html')


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'productPage.html', context)


class HomeView(ListView):
    model = Item
    paginate_by = 5
    template_name = "homePage.html"


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'orderSummary.html', context)
        except ObjectDoesNotExist:
            messages.error((self.request), "Seems like like you dont have anything in your cart...!!!")
            return redirect('/')

    # model = Order
    # template_name = 'orderSummary.html'


class CheckoutView(TemplateView):
    model = Item
    template_name = "checkoutPage"


class ProductView(DetailView):
    model = Item
    template_name = "productPage.html"

@login_required
def addToCart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        items=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(items__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Item quantity updated...!!!")
            return redirect('Ecom:Order Summary')
        else:
            order.items.add(order_item)
            messages.info(request, "Item added to your cart...!!!")
            return redirect('Ecom:Order Summary')
    else:
        order_date = timezone.now()
        order = Order.objects.create(user=request.user, orderedDate=order_date)
        order.items.add(order_item)
        messages.info(request, "Item added to your cart...!!!")
        return redirect('Ecom:Order Summary')

@login_required
def removeFromCart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(items__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                items=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.save()
            messages.info(request, "Item removed from your cart..!!!")
            return redirect('Ecom:Order Summary')
        else:
            # Add message saying order doesn't have required item
            messages.info(request, "Item is not in your cart..!!!")
            return redirect('Ecom:Product Details', slug=slug)
    else:
        # Add message saying user doesn't have an order
        messages.info(request, "Your cart is empty..!!!")
        return redirect('Ecom:Product Details', slug=slug)
    return redirect('Ecom:Product Details', slug=slug)

@login_required
def removeSingleItemFromCart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(items__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                items=item,
                user=request.user,
                ordered=False
            )[0]
            order_item.quantity-=1
            order_item.save()
            messages.info(request, "Item quantity is  updated in your cart..!!!")
            return redirect('Ecom:Order Summary')
        else:
            # Add message saying order doesn't have required item
            messages.info(request, "Item is not in your cart..!!!")
            return redirect('Ecom:Order Summary')
    else:
        # Add message saying user doesn't have an order
        messages.info(request, "Your cart is empty..!!!")
        return redirect('Ecom:Product Details', slug=slug)

