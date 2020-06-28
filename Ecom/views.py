from django.shortcuts import render
from .models import Item

def itemList(request):
    context={
        'item': Item.objects.all()
    }
    return render(request,"homePage.html",context)