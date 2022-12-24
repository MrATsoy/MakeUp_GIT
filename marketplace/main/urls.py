from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('show_categories/', show_categories, name='cats'),
    path('basket/', basket, name='basket'),
    path('post/<slug:post_slug>/', show_post, name='show_post')
]
