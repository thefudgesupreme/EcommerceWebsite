from django.shortcuts import render
from .models import Item
from django.views.generic import ListView,DetailView,TemplateView


def home(request):
    context={
        'items': Item.objects.all()
    }
    return render(request,"homePage.html",context)

def checkout(request):
    return render(request,'checkoutPage.html')

def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request,'productPage.html',context)

class HomeView(ListView):
    model = Item
    template_name = "homePage.html"

class CheckoutView(TemplateView):
    model = Item
    template_name = "checkoutPage"

class ProductView(DetailView):
    model = Item
    template_name = "productPage.html"