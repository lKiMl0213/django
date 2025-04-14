from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from datetime import datetime
from .models import Product

def estoque_view(request):
    return render(request, 'estoque/storage.html')

@require_http_methods(["GET", "POST"])
def manage_product(request):
    if request.method == 'GET':
        action = request.GET.get('action')
        if not action:
            return render(request, 'storage.html')

        if action == 'check_barcode':
            barcode = request.GET.get('barcode')
            try:
                product = Product.objects.get(barcode=barcode)
                return JsonResponse({
                    'exists': True,
                    'barcode': product.barcode,
                    'name': product.name,
                    'buy_price': float(product.buy_price),
                    'sell_price': float(product.sell_price),
                    'stock': product.stock,
                    'month': str(product.expiration_date.month).zfill(2),
                    'year': str(product.expiration_date.year)
                })
            except Product.DoesNotExist:
                return JsonResponse({'exists': False})

        elif action == 'low_stock':
            products = Product.objects.filter(stock__lt=10)
            return JsonResponse({
                'success': True,
                'products': [
                    {'barcode': p.barcode, 'name': p.name, 'stock': p.stock}
                    for p in products
                ]
            })

        elif action == 'expiration_date_verify':
            from django.utils.timezone import now
            from dateutil.relativedelta import relativedelta
            limit_date = now().date() + relativedelta(months=2)
            products = Product.objects.filter(expiration_date__lt=limit_date)
            return JsonResponse({
                'success': True,
                'products': [
                    {'barcode': p.barcode, 'name': p.name, 'expiration_date': p.expiration_date.strftime('%Y-%m-%d')}
                    for p in products
                ]
            })

        elif action == 'list_products':
            products = Product.objects.all().order_by('name')
            return JsonResponse({
                'success': True,
                'products': [
                    {
                        'barcode': p.barcode,
                        'name': p.name,
                        'buy_price': float(p.buy_price),
                        'sell_price': float(p.sell_price),
                        'stock': p.stock,
                        'expiration_date': p.expiration_date.strftime('%m/%Y')
                    }
                    for p in products
                ]
            })

    elif request.method == 'POST':
        action = request.GET.get('action')
        if not action:
            return render(request, 'storage.html')

        if action == 'add_product':
            data = request.POST
            required_fields = ['barcode', 'name', 'buy_price', 'sell_price', 'stock', 'month', 'year']
            if not all(field in data and data[field].strip() for field in required_fields):
                return JsonResponse({'success': False, 'message': "Todos os campos são obrigatórios."})

            try:
                expiration_date = datetime.strptime(
                    f"{data['year']}-{data['month'].zfill(2)}-01", '%Y-%m-%d'
                ).date()
            except ValueError:
                return JsonResponse({'success': False, 'message': "Data inválida."})

            product, created = Product.objects.update_or_create(
                barcode=data['barcode'],
                defaults={
                    'name': data['name'],
                    'buy_price': data['buy_price'],
                    'sell_price': data['sell_price'],
                    'stock': data['stock'],
                    'expiration_date': expiration_date
                }
            )

            msg = "Produto cadastrado com sucesso." if created else "Produto atualizado com sucesso."
            return JsonResponse({'success': True, 'message': msg})

        elif action == 'remove_product':
            barcode = request.POST.get('barcode')
            if not barcode:
                return JsonResponse({'success': False, 'message': "Código de barras é obrigatório."})

            try:
                product = Product.objects.get(barcode=barcode)
                product.delete()
                return JsonResponse({'success': True, 'message': "Produto removido com sucesso."})
            except Product.DoesNotExist:
                return JsonResponse({'success': False, 'message': "Produto não encontrado."})
