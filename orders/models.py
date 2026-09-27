from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='cart')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Cart"

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    def get_total_price(self):
        return self.product.price * self.quantity

class Order(models.Model):
    STATUS_CHOICE = [
        ('Pending','Pending'),
        ('Processing','Processing'),
        ('Shipped','Shipped'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled'),
    ]

    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders')
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=20,choices=STATUS_CHOICE,default='Pending')
    address=models.TextField()
    phone=models.CharField(max_length=15)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Order #{self.id} - {self.user.username}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()

    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    def get_total_price(self):
        return self.price * self.quantity

    
    