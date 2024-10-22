"""
Definition of views.
"""
from django.contrib.auth.decorators import login_required
from .models import Customer, Product, Category,Wishlist, WishlistItem
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
def search(request):
    """Handles search queries and displays search results."""
    assert isinstance(request, HttpRequest)
    
    query = request.GET.get('q', '')  # Get the search query from the GET request
    
    if query:
        # Split the query into individual keywords
        keywords = query.split()
        
        # Build a Q object to filter products containing any of the keywords
        from django.db.models import Q
        query_filter = Q()
        for keyword in keywords:
            query_filter |= Q(name__icontains=keyword)  # Case-insensitive search
        
        # Apply the filter to the Product model
        results = Product.objects.filter(query_filter)
    else:
        results = Product.objects.none()  # No results if query is empty

    


    return render(
        request,
        'app/search.html',
        {
            'title': 'Search Results',
            'message': f'Results for "{query}"',
            'year': datetime.now().year,
            'products': results,  # Pass search results to the template
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def women(request):
    """Renders the womens page with items from the womens category."""
    assert isinstance(request, HttpRequest)

    # Fetch the 'womens' category using lowercase
    womens_category = get_object_or_404(Category, category_name='womens')

    # Fetch products belonging to the 'womens' category
    products = Product.objects.filter(category=womens_category)

    color_filter = request.GET.get('color')
    size_filter = request.GET.get('size')
    type_filter = request.GET.get('type')
    price_order = request.GET.get('price_order')

    if color_filter:
        products = products.filter(color=color_filter)
    if size_filter:
        products = products.filter(size=size_filter)
    if type_filter:
        products = products.filter(type=type_filter)
    if price_order:
        if price_order == 'cheapest_first':
            products = products.order_by('price')
        elif price_order == 'expensive_first':
            products = products.order_by('-price')



    return render(
        request,
        'app/women.html',
        {
            'title': 'Womens',
            'message': 'Womens items available here',
            'year': datetime.now().year,
            'products': products,  # Pass filtered items to the template
        }
    )

def men(request):
    """Renders the Mens page."""
    assert isinstance(request, HttpRequest)

    # Fetch the 'mens' category using lowercase
    mens_category = get_object_or_404(Category, category_name='mens')

    # Fetch products belonging to the 'mens' category
    products = Product.objects.filter(category=mens_category)

    color_filter = request.GET.get('color')
    size_filter = request.GET.get('size')
    type_filter = request.GET.get('type')
    price_order = request.GET.get('price_order')

    if color_filter:
        products = products.filter(color=color_filter)
    if size_filter:
        products = products.filter(size=size_filter)
    if type_filter:
        products = products.filter(type=type_filter)
    if price_order:
        if price_order == 'cheapest_first':
            products = products.order_by('price')
        elif price_order == 'expensive_first':
            products = products.order_by('-price')


    return render(
        request,
        'app/men.html',
        {
            'title':'Mens',
            'message':'Mens items available here',
            'year':datetime.now().year,
            'products': products,
        }
    )

def kids(request):
    """Renders the kids page."""
    assert isinstance(request, HttpRequest)

    # Fetch the 'kids' category using lowercase
    kids_category = get_object_or_404(Category, category_name='kids')

    # Fetch products belonging to the 'kids' category
    products = Product.objects.filter(category=kids_category)

    color_filter = request.GET.get('color')
    size_filter = request.GET.get('size')
    type_filter = request.GET.get('type')
    price_order = request.GET.get('price_order')

    if color_filter:
        products = products.filter(color=color_filter)
    if size_filter:
        products = products.filter(size=size_filter)
    if type_filter:
        products = products.filter(type=type_filter)
    if price_order:
        if price_order == 'cheapest_first':
            products = products.order_by('price')
        elif price_order == 'expensive_first':
            products = products.order_by('-price')

    return render(

        request,
        'app/kids.html',
        {
            'title':'Kids',
            'message':'Kids items available here',
            'year':datetime.now().year,
            'products': products,
        }
    )

def shoes(request):
    """Renders the Shoes page."""
    assert isinstance(request, HttpRequest)

    # Fetch the 'shoes' category using lowercase
    shoes_category = get_object_or_404(Category, category_name='shoes')

    # Fetch products belonging to the 'shoes' category
    products = Product.objects.filter(category=shoes_category)

    color_filter = request.GET.get('color')
    size_filter = request.GET.get('size')
    type_filter = request.GET.get('type')
    price_order = request.GET.get('price_order')

    if color_filter:
        products = products.filter(color=color_filter)
    if size_filter:
        products = products.filter(size=size_filter)
    if type_filter:
        products = products.filter(type=type_filter)
    if price_order:
        if price_order == 'cheapest_first':
            products = products.order_by('price')
        elif price_order == 'expensive_first':
            products = products.order_by('-price')

    return render(
        request,
        'app/shoes.html',
        {
            'title':'Shoes',
            'message':'Shoes items available here',
            'year':datetime.now().year,
            'products': products,
        }
    )

def accessories(request):
    """Renders the Accessories page."""
    assert isinstance(request, HttpRequest)

    # Fetch the 'accessories' category using lowercase
    accessories_category = get_object_or_404(Category, category_name='accessories')

    # Fetch products belonging to the 'accessories' category
    products = Product.objects.filter(category=accessories_category)

    color_filter = request.GET.get('color')
    size_filter = request.GET.get('size')
    type_filter = request.GET.get('type')
    price_order = request.GET.get('price_order')

    if color_filter:
        products = products.filter(color=color_filter)
    if size_filter:
        products = products.filter(size=size_filter)
    if type_filter:
        products = products.filter(type=type_filter)
    if price_order:
        if price_order == 'cheapest_first':
            products = products.order_by('price')
        elif price_order == 'expensive_first':
            products = products.order_by('-price')

    return render(
        request,
        'app/accessories.html',
        {
            'title':'Accessories',
            'message':'Accessories items available here',
            'year':datetime.now().year,
            'products': products,
        }
    )

def cart(request):
    """Renders the Cart page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cart.html',
        {
            'title':'Your Cart',
            'message':'View Your Cart Items Here',
            'year':datetime.now().year,
        }
    )
@login_required
def wishlist(request):
    """Render the customer's wishlist."""
    user = request.user
    try:
        # Retrieve the customer associated with the logged-in user
        customer = Customer.objects.get(user=user)
    except Customer.DoesNotExist:
        customer = None

    # Fetch the wishlist associated with the customer
    wishlist = Wishlist.objects.filter(customer=customer).first() if customer else None
    wishlist_items = WishlistItem.objects.filter(wishlist=wishlist) if wishlist else []

    return render(request, 'app/wishlist.html', {
        'title': 'Wishlist Details',
        'wishlist_items': wishlist_items,
        'year': datetime.now().year,
    })

@login_required
def add_to_wishlist(request, product_id):
    """Add a product to the user's wishlist."""
    user = request.user
    product = get_object_or_404(Product, product_id=product_id)
    
    # Get or create the wishlist for the user
    wishlist, created = Wishlist.objects.get_or_create(user=user)
    
    # Check if the product is already in the wishlist
    if not WishlistItem.objects.filter(wishlist=wishlist, product=product).exists():
        WishlistItem.objects.create(wishlist=wishlist, product=product)
    
    return redirect('wishlist')

@login_required(login_url='/login/')
def account(request):
    """Renders the Cart page."""
    assert isinstance(request, HttpRequest)
    user = request.user
    return render(
        request,
        'app/account.html',
        {
            'title':'Welcome to your Profile Page!',
            'message':'View Your Account Details Here',
            'year':datetime.now().year,
            'user': user  # Pass the user object to the template
        }
    )