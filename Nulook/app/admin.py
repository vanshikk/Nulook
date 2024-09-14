# app/admin.py

from django.contrib import admin
from .models import Product, Category, Wishlist, WishlistItem

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'wishlist', 'product')
