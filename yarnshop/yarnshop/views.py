from django.shortcuts import render


def main(request):
    content = {
        'topic': 'тренды',
        'tittle': 'Магазин',
    }

    return render(request, 'index.html', context=content)


def contact(request):
    content = {
        'tittle': 'Контакты',
    }

    return render(request, 'contact.html', context=content)
