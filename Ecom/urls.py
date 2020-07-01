from django.urls import path
from .views import CheckoutView, ProductView, HomeView,home,checkout

app_name = 'Ecom'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', checkout, name='Checkout'),
    path('product/<slug>', ProductView.as_view(), name='Product Details')
]
