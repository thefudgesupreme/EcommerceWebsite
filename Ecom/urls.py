from django.urls import path
from .views import itemList

app_name = 'Ecom'

urlpatterns = [
    path('', itemList, name='itemList')
]
