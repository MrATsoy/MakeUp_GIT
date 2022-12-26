from .models import *

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Обратная связь', 'url_name': 'basket'},
    {'title': 'Корзина', 'url_name': 'basket'},
]

class DataMixin:
    paginate_by = 6
    def get_user_context(self, **kwargs):
       context = kwargs
       cats = Category.objects.all()
       context ['menu'] = menu
       context ['cats'] = cats

       return context