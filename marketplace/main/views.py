from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
# Create your views here.

menu = [
    {'title': 'Главная', 'url_name': 'home'},

    {'title': 'Корзина', 'url_name': 'basket'},
]


def index(request):
    products = Product.objects.all()
    context = {
        'menu': menu,
        'products': products,
    }
    return render(request, 'main/index.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Product, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
    }
    return render(request, 'main/show_post.html', context=context)


def basket(request):
    return HttpResponse('basket')


def show_categories(request, cat_slug):
    products = Product.objects.filter(cat__slug=cat_slug)
    context = {
        'menu': menu,
        'products': products
    }
    return render(request, 'main/index.html', context=context)











































