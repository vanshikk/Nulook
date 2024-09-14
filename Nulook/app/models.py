"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

# Category Table
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255) #womens, mens etc for the pages

    def __str__(self):
        return self.name


# Product Table
class Product(models.Model):
    #clothing sizes
    SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('2XL', '2X Large'),
        ('3XL', '3X Large'),
        ('4XL', '4X Large'),
    ]


    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=50)  # e.g., Pants, Shirt, etc.
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')  # Add this line for the image path

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly define the ID field
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"

class WishlistItem(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly define the ID field
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} in {self.wishlist.user.username}'s Wishlist"


