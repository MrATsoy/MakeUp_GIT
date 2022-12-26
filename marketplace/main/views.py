from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

from .forms import RegisterUserForm, AddProductForm
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




class ShowPost(DataMixin, DeleteView):
    model = Product
    template_name = 'main/show_post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="NameSite")
        return dict(list(context.items()) + list(c_def.items()))



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


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="NameSite")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


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



def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddProductForm()
    context = {
        'menu': menu,
        'form': form
    }
    return render(request, 'main/add_product.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('home')


def basket(request):
    return render(request, 'main/')











































