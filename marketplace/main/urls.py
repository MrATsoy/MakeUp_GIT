from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductHome.as_view(), name='home'),
    path('show_categories/<slug:cat_slug>/', ProductCategories.as_view(), name='cats'),
    path('basket/', basket, name='basket'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='show_post'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout')
]
