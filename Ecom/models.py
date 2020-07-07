from django.conf import settings
from django.db import models
from datetime import datetime

from django.urls import reverse

CATEGORY_CHOICES=(
    ('S','Shirt'),
    ('SW','Sports Wear'),
    ('OW','Out Wear'),
)

LABEL_CHOICES=(
    ('P','primary'),
    ('S','secondary'),
    ('D','danger'),
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price=models.FloatField()
    discount_price=models.FloatField(blank=True,null=True)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    label=models.CharField(choices=LABEL_CHOICES,max_length=1)
    slug=models.SlugField()
    description=models.TextField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Ecom:Product Details",kwargs={'slug':self.slug})

    def get_addToCart_url(self):
        return reverse('Ecom:Add To Cart', kwargs={
            'slug':self.slug
        })

    def get_removeFromCart_url(self):
        return reverse('Ecom:Remove From Cart', kwargs={
            'slug':self.slug
        })

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items=models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of Item : {self.items.title}"

    def calculateTotalPrice(self):
            return self.items.price  *  self.quantity

    def calculateDiscountPrice(self):
            return (self.items.discount_price * self.quantity).__float__()

    def totalAmountSaved(self):
            return (self.calculateTotalPrice() - self.calculateDiscountPrice()).__float__()

    def finalPrice(self):
        if self.items.discount_price:
            return self.calculateDiscountPrice()
        return self.calculateTotalPrice()

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    startDate = models.DateTimeField(default=datetime.now)
    orderedDate=models.DateTimeField(default=datetime.now)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.__str__()

    def totalOrderPrice(self):
        total=0
        for item in self.items.all():
            total+=OrderItem.finalPrice(item)
        return total