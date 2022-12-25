from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('show_categories/<slug:cat_slug>/', show_categories, name='cats'),
    path('basket/', basket, name='basket'),
    path('post/<slug:post_slug>/', show_post, name='show_post'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout')
]
