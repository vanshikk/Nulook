"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


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
    customer = models.OneToOneField('Customer', on_delete=models.CASCADE, related_name='payment_method_for_customer')
    card_number = models.CharField(max_length=16, blank=True, null=True)  # Optional for credit card
    payment_type = models.CharField(max_length=50)  # Changed to payment_type
    card_expiry_date = models.DateField(blank=True, null=True)  # Optional for credit card
    mpaisa_number = models.CharField(max_length=15, blank=True, null=True)  # Optional for M-Paisa
    mpaisa_pin = models.CharField(max_length=6, blank=True, null=True)  # Optional for M-Paisa


# Customer Model
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_username = models.CharField(max_length=255, unique=True, null=True)
    customer_first_name = models.CharField(max_length=100, blank=True, null=True)
    customer_last_name = models.CharField(max_length=100, blank=True, null=True)
    customer_email = models.EmailField(unique=True, null=True, blank=True)  # Allow null values
    customer_password = models.CharField(max_length=255, blank=True, null=True)
    customer_gender = models.CharField(
        max_length=20, 
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Rather Not Say', 'Rather Not Say')], 
        blank=True
    )
    customer_date_of_birth = models.DateField( null=True)
    customer_phone = models.CharField(max_length=15, blank=True, null=True)
    payment_method = models.OneToOneField('PaymentMethod', on_delete=models.CASCADE, related_name='customer_payment_method', blank=True, null=True)



class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_username = models.CharField(max_length=255, unique=True, null=True)
    employee_first_name = models.CharField(max_length=100, null=True)
    employee_last_name = models.CharField(max_length=100, null=True)
    employee_email = models.EmailField(unique=True, null=True)
    employee_password = models.CharField(max_length=255, null=True)
    employee_gender = models.CharField(
        max_length=20, 
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Rather Not Say', 'Rather Not Say')]
    , null=True)
    employee_date_of_birth = models.DateField( null=True)
    employee_phone = models.CharField(max_length=15, null=True)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_type = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='product_images/', default='product_images/notfound.jpg')
    product_colour = models.ManyToManyField(Colour)

    def total_stock(self):
        return sum(size.stock for size in self.product_sizes.all())  # Aggregates stock from all sizes

class ProductSize(models.Model):
    product = models.ForeignKey(Product, related_name='product_sizes', on_delete=models.CASCADE)
    size = models.CharField(max_length=50)  # e.g., "S", "M", "L"
    stock = models.PositiveIntegerField()  # Stock for this specific size

    class Meta:
        unique_together = ('product', 'size')  # Ensures each product has unique size entries




class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    cart_total = models.DecimalField(max_digits=10, decimal_places=2)  # Total cost of items in the cart (excluding VAT)

    def calculate_cart_total(self):
        total = sum(item.product.product_price * item.item_quantity for item in self.cartitem_set.all())
        vat = total * 0.15  # 15% VAT calculation
        return total + vat


class CartItem(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    item_quantity = models.PositiveIntegerField()

    def item_total(self):
        return self.product.product_price * self.item_quantity  # Total cost per item


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

