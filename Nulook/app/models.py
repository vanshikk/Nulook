"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Change related name here to avoid conflict with 'user_set'
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
        related_query_name='customuser',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  # Change related name here to avoid conflict with 'user_permissions'
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
        related_query_name='customuser',
    )


class Colour(models.Model):
    color_name = models.CharField(max_length=50)

    def __str__(self):
        return self.color_name

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class PaymentMethod(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer = models.OneToOneField('Customer', on_delete=models.CASCADE, related_name='payment_method')
    card_number = models.CharField(max_length=16, blank=True, null=True)  # Optional for credit card
    payment_type = models.CharField(max_length=50)  # Changed to payment_type
    card_expiry_date = models.DateField(blank=True, null=True)  # Optional for credit card
    mpaisa_number = models.CharField(max_length=15, blank=True, null=True)  # Optional for M-Paisa
    mpaisa_pin = models.CharField(max_length=6, blank=True, null=True)  # Optional for M-Paisa

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    customer_gender = models.CharField(max_length=10)  # Added gender field
    date_of_birth = models.DateField()  # User-defined

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    employee_gender = models.CharField(max_length=10)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_type = models.CharField(max_length=100)
    product_stock = models.PositiveIntegerField()
    product_color = models.ManyToManyField(Colour)
    
    product_size = models.CharField(max_length=50)  # Keeping size field
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='product_images/', default='product_images/notfound.jpg')


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    cart_total = models.DecimalField(max_digits=10, decimal_places=2)

class CartItem(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    item_quantity = models.PositiveIntegerField()

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)

class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_item_quantity = models.PositiveIntegerField()
    order_item_price = models.DecimalField(max_digits=10, decimal_places=2)

class Wishlist(models.Model):
    wishlist_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class WishlistItem(models.Model):
    wishlist_item_id = models.AutoField(primary_key=True)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

