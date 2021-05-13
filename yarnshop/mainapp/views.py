from django.shortcuts import render
from .models import ProductCategory, Product


def products(request, pk=None):
    links_menu = {'links': [
        {'href': 'index', 'name': 'все'},
        {'href': 'index', 'name': 'дом'},
        {'href': 'index', 'name': 'офис'},
        {'href': 'index', 'name': 'классика'},
        {'href': 'index', 'name': 'модерн'},
    ]}

    return render(request, 'mainapp/products.html', context=links_menu)



