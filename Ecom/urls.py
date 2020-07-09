from django.urls import path
from .views import (ProductView, HomeView,
                                CheckoutView, addToCart, removeFromCart,
                                OrderSummaryView,removeSingleItemFromCart)

app_name = 'Ecom'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='Checkout'),
    path('product/<slug>', ProductView.as_view(), name='Product Details'),
    path('order-summary/', OrderSummaryView.as_view(), name='Order Summary'),
    path('incart/<slug>', addToCart, name='Add To Cart'),
    path('outcart/<slug>', removeFromCart, name='Remove From Cart'),
    path('singleoutcart/<slug>', removeSingleItemFromCart, name='Remove Single Item Cart'),
]
