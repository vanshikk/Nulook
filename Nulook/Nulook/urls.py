"""
Definition of urls for Nulook.
"""

from datetime import datetime
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from app import forms, views


urlpatterns = [

    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('women/', views.women, name='women'),
    path('men/', views.men, name='men'),
    path('kids/', views.kids, name='kids'),
    path('shoes/', views.shoes, name='shoes'),
    path('cart/', views.cart, name='cart'),
    path('account/', views.account, name='account'),
     path('wishlist/', views.wishlist, name='wishlist'),
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('accessories/', views.accessories, name='accessories'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
