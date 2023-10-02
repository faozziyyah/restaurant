from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255, db_index=True)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateField(db_index=True)

class Menu(models.Model):
    Title = models.CharField(max_length=255, db_index=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    Inventory = models.IntegerField()

#class Cart(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
#    quantity = models.SmallIntegerField()
#    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
#    price = models.DecimalField(max_digits=6, decimal_places=2)
#
#    class Meta:
#        unique_together = ('menuitem', 'user')
#
#class Order(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    delivery_crew = models.ForeignKey(User, on_delete=models.CASCADE, related_name='delivery_crew', null=True)
#    status = models.BooleanField(db_index=True, default=0)
#    total = models.DecimalField(max_digits=6, decimal_places=2)
#    date = models.DateField(db_index=True)
#
#class OrderItem(models.Model):
#    order = models.ForeignKey(User, on_delete=models.CASCADE)
#    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
#    quantity = models.SmallIntegerField()
#    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
#    price = models.DecimalField(max_digits=6, decimal_places=2)
#
#    class Meta:
#        unique_together = ('order', 'menuitem')
#