from django.conf import settings
from django.db import models
from datetime import datetime


class Item(models.Model):
    title = models.CharField(max_length=100)
    price=models.FloatField(default=0.0)
    def __str__(self):
        return self.title


class OrderItem(models.Model):
    items=models.ForeignKey(Item,on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    startDate = models.DateTimeField(default=datetime.now)
    orderedDate=models.DateTimeField(default=datetime.now)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.title