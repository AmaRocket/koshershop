from django import forms
from django.contrib import admin
from django.forms import ModelChoiceField

from .models import *


class CakeAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='Cake'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class BaketyAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='Bekery'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)

admin.site.register(Bakery, BaketyAdmin)
admin.site.register(Cake, CakeAdmin)

admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
