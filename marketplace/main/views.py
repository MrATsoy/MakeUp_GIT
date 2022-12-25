from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm
from .models import *
# Create your views here.

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Обратная связь', 'url_name': 'basket'},
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


def login(request):
    return HttpResponse('login')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')












































