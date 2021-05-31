from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product
from basketapp.models import Basket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    all_products = Product.objects.all()

    return random.sample(list(all_products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def products(request, pk=None, page=1):
    print(pk)
    category = ''
    products = ''

    categories = ProductCategory.objects.filter(is_active=True)
    basket = get_basket(request.user)
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    if pk is not None:
        if pk == 0:
            category = {
                'pk': 0,
                'name': 'все',
            }
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')

        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category_id__pk=pk, is_active=True, category__is_active=True).order_by('price')

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': 'Категория продукта',
            'categories': categories,
            'category': category,
            'products': products_paginator,
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', content)

    context = {
        'title': 'продукты',
        'categories': categories,
        'category': category,
        'products': products,
        'basket': basket,
        'hot_product': hot_product,
        'same_products': same_products,
    }

    return render(request, 'mainapp/products.html', context=context)


def product(request, pk):

    content = {
        'title': 'страница продукта',
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', context=content)

