from django.db import models

# Order Model Table
class Order(models.Model):
    order_id = models.CharField(max_length=50, unique=True)
    note = models.TextField()
    customer_name = models.CharField(max_length=100)
    total_order_amount = models.DecimalField(decimal_places=2, max_digits=10)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.order_id} order status: {self.is_paid}"

    
# OrderItem Model Table
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True)
    item_name = models.CharField(max_length=100)
    item_price = models.DecimalField(decimal_places=2, max_digits=10)
    qnty = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name


from .models import User, Menu
from django.db import models

class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    customer = models.CharField(max_length=100)
    order_items = models.CharField(max_length=500)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    order_status = models.CharField(max_length=15, choices=ORDER_STATUS_CHOICES)

    def __str__(self):
        return f"(self.customer) total payable amount: {self.total_amount}"


# API
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Menu
from .serializers import MenuSerializer

class MenuListAPI(APIView):
    def get(self, request):
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        return Response(serializer.data)    


# url

from django.urls import path
from .views import MenuListAPI

urlpatterns = [
    path('api/menu/', MenuListAPI.as_view(), name='menu-list'),
]


# display menu on template

import requests
from django.shortcuts import render

def home_view(request):
    try:
        response = requests.get("http://localhost:8000/api/menu")
        menu_data = response.json()
    except:
        menu_data = []

    return render(request, 'home/home.html', {'menu': menu_data})



# admin panel

from django.contrib import admin
from .models import Menu , Order

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    fields = '__all__'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = '__all__'
    
#-------------------------------------------------------------------------------------------------------------------------

# views.py

from django.shortcuts import render
from .models import Restaurant

def home(request):
    restaurant = Restaurant.objects.first()
    restaurant_name = restaurant.name if restaurant else "My Restaurant"
    return render(request, 'home/home.html', {'restaurant_name':restaurant_name})
