import json

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from geekshop.settings import BASE_DIR
from mainapp.models import Product, Category
from mainapp.services import get_basket, get_hot_product, get_same_products


def index(request):
    context = {
        'products': Product.objects.all()[:4],
        'basket': get_basket(request.user)
    }

    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    print(pk)
    links_menu = Category.objects.all()
    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all()
            category_item = {'name': 'все', 'pk': 0}
        else:
            products_list = Product.objects.filter(category_id=pk)
            category_item = get_object_or_404(Category, pk=pk)

        page = request.GET.get('page')
        paginator = Paginator(products_list, 2)
        try:
            paginated_products = paginator.page(page)
        except PageNotAnInteger:
            paginated_products = paginator.page(1)
        except EmptyPage:
            paginated_products = paginator.page(paginator.num_pages)

        context = {
            'links_menu': links_menu,
            'products': paginated_products,
            'category': category_item,
            'basket': get_basket(request.user)
        }


        return render(request, 'mainapp/products_list.html', context)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    context = {
        'links_menu': links_menu,
        'basket': get_basket(request.user),
        'hot_product': hot_product,
        'same_products': same_products
    }

    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    context = {
        'links_menu': Category.objects.all(),
        'product': product_item,
        'basket': get_basket(request.user)
    }

    return render(request, 'mainapp/product.html', context)


def contact(request):
    with open(f'{BASE_DIR}/contacts.json', encoding="utf-8") as contacts_json:
        contacts = json.load(contacts_json)

        context = {
            'contacts': contacts,
            'basket': get_basket(request.user)
        }

    return render(request, 'mainapp/contact.html', context)
