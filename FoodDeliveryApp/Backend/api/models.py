from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    cuisine = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.restaurant_name

class FoodItem(models.Model):
    food_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=255)
    food_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.FloatField()
    availability = models.CharField(max_length=50, choices=[('Available', 'Available'), ('Out of Stock', 'Out of Stock')], default='Available')

    def __str__(self):
        return self.food_name

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    food_name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    total_price = models.FloatField()

    def __str__(self):
        return f"{self.customer_name} - {self.food_name}"

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    restaurant_name = models.CharField(max_length=255)
    order_items = models.TextField()
    total_amount = models.FloatField()
    payment_status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending')
    delivery_status = models.CharField(max_length=50, choices=[('Preparing', 'Preparing'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Preparing')

    def __str__(self):
        return f"Order {self.order_id} by {self.customer_name}"
