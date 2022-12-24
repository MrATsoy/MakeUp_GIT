from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'photo')
    search_fields = ('title', 'content')
    list_editable = ('photo',)
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
