from django.shortcuts import render
from mainapp.models import ProductCategory, Product


def main(request):
    title = 'главная'
    products = Product.objects.all()[:4]
    content = {
        'title': title,
        'products': products
    }

    return render(request, 'index.html', context=content)


def contact(request):
    content = {
        'tittle': 'Контакты',
    }
    return render(request, 'contact.html', context=content)

