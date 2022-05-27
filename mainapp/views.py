import json

from django.shortcuts import render

from geekshop.settings import BASE_DIR
from mainapp.models import Product, Category


def index(request):
    context = {
        'products': Product.objects.all()[:4]
    }

    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'links_menu': Category.objects.all()
    }
    return render(request, 'mainapp/products.html', context)


def products_list(request, pk):
    print(pk)
    context = {
        'links_menu': Category.objects.all()
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    with open(f'{BASE_DIR}/contacts.json', encoding="utf-8") as contacts_json:
        contacts = json.load(contacts_json)

        context = {
            'contacts': contacts
        }

    return render(request, 'mainapp/contact.html', context)
