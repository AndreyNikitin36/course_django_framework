from django.shortcuts import render
from mainapp.models import ProductCategory, Product

from basketapp.models import Basket


def main(request):
    title = 'главная'
    products = Product.objects.all()[:4]
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    content = {
        'title': title,
        'products': products,
        'basket': basket,
    }

    return render(request, 'index.html', context=content)


def contact(request):
    content = {
        'tittle': 'Контакты',
    }
    return render(request, 'contact.html', context=content)

