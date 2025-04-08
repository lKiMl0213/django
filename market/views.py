from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import AddToCartForm
from django.contrib import messages

def home_view(request):
    return render(request, 'market/market.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'market/products.html', {'products': products})

def add_to_cart(request):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data['barcode']
            quantity = form.cleaned_data['quantity']
            product = get_object_or_404(Product, barcode=barcode)

            if product.stock >= quantity:
                cart = request.session.get('cart', [])
                cart.append({
                    'barcode': product.barcode,
                    'name': product.name,
                    'price': float(product.price),
                    'quantity': quantity,
                    'total': float(product.price) * quantity
                })
                request.session['cart'] = cart
                messages.success(request, f"{product.name} adicionado ao carrinho.")
            else:
                messages.error(request, "Estoque insuficiente.")
        return redirect('product_list')

def view_cart(request):
    cart = request.session.get('cart', [])
    subtotal = sum(item['total'] for item in cart)
    return render(request, 'market/cart.html', {'cart': cart, 'subtotal': subtotal})

def checkout(request):
    cart = request.session.get('cart', [])
    if not cart:
        messages.error(request, "Carrinho vazio.")
        return redirect('product_list')

    for item in cart:
        product = Product.objects.get(barcode=item['barcode'])
        product.stock -= item['quantity']
        product.save()

    request.session['cart'] = []
    messages.success(request, "Compra finalizada!")
    return redirect('product_list')
