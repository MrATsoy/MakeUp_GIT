from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import RegisterUserForm
from .models import *
from .utils import *
# Create your views here.


class ProductHome(DataMixin, ListView):
    model = Product
    template_name = 'main/index.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="NameSite")
        return dict(list(context.items()) + list(c_def.items()))




def show_post(request, post_slug):
    post = get_object_or_404(Product, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
    }
    return render(request, 'main/show_post.html', context=context)


class ProductCategories(DataMixin, ListView):
    model = Product
    template_name = 'main/index.html'
    context_object_name = 'products'
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=" NameSite")
        return dict(list(context.items()) + list(c_def.items()))


def login(request):
    return HttpResponse('login')

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="NameSite")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


def basket(request):
    return render(request, 'main/')











































