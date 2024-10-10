# app/admin.py

from django.contrib import admin
from .models import CustomUser, Category, PaymentMethod, Customer, Employee, Product, Cart, CartItem, Order, OrderItem, Wishlist, WishlistItem, Colour

# Registering all models without custom ModelAdmin classes
admin.site.register(Colour)
admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(PaymentMethod)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Wishlist)
admin.site.register(WishlistItem)
