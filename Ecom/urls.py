from django.urls import path
from .views import (CheckoutView, ProductView, HomeView
                                ,home,checkout,addToCart,removeFromCart)
                                # userSignup,userLogin)

app_name = 'Ecom'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', checkout, name='Checkout'),
    path('product/<slug>', ProductView.as_view(), name='Product Details'),
    path('incart/<slug>', addToCart, name='Add To Cart'),
    path('outcart/<slug>', removeFromCart, name='Remove From Cart'),
    # path('/signin', userLogin, name='Login'),
    # path('/signup', userSignup, name='Signup'),
]
