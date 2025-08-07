from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharaField(max_length=15)

    def __str__(self):
        return self.name



# restaurant order model

from models import User, Menu
from django.db import models

class Order(models.Model):

    ORDER_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In_Progress'),
        ('completed', 'Completed'),
        ('deleted', 'Deleted'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=model.CASCADE)
    customer = models.CharaField(max_length=100)
    order_item = models.CharaField(max_length=500)
    total_amount = models.DecimalField(max_digits = 8, decimal_places=2)
    order_status = models.CharaField(max_length=15, choices=ORDER_CHOICES)

    def __str__(self):
        return f"{self.customer} , Total payable amount: {self.total_amount}"