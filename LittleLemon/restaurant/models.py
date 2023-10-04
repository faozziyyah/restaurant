from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255, db_index=True)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateField(db_index=True)

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self)-> str:
        return self.title

class MenuItem(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    def __str__(self)-> str:
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.CASCADE, related_name='delivery_crew', null=True)
    status = models.BooleanField(db_index=True, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(db_index=True)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem_id =  models.SmallIntegerField()
    rating = models.SmallIntegerField()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('menuitem', 'user')


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('order', 'menuitem')
