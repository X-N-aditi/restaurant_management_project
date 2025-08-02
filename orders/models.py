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
