from django import forms
from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.utils.safestring import mark_safe

from .models import *
from PIL import Image


class CakeAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            f"""<span style='color:red; font-size:14px;'>Uploading image with resolution more than :
            {Product.MAX_RESOLUTION[0]} x {Product.MAX_RESOLUTION[1]} picture will be cropped </span>""")


class CakeAdmin(admin.ModelAdmin):
    form = CakeAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='cake'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class BakeryAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            f"""<span style='color:red; font-size:14px;'>Uploading image with resolution more than :
            {Product.MAX_RESOLUTION[0]} x {Product.MAX_RESOLUTION[1]} picture will be cropped </span>""")

class BakeryAdmin(admin.ModelAdmin):
    form = BakeryAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='bakery'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class BreadAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            f"""<span style='color:red; font-size:14px;'>Uploading image with resolution more than :
            {Product.MAX_RESOLUTION[0]} x {Product.MAX_RESOLUTION[1]} picture will be cropped </span>""")

class BreadAdmin(admin.ModelAdmin):
    form = BreadAdminForm
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='bread'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SemiFinishedAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            f"""<span style='color:red; font-size:14px;'>Uploading image with resolution more than :
            {Product.MAX_RESOLUTION[0]} x {Product.MAX_RESOLUTION[1]} picture will be cropped </span>""")

class SemiFinishedAdmin(admin.ModelAdmin):
    form = SemiFinishedAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='semifinishedproducts'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)

admin.site.register(Bakery, BakeryAdmin)
admin.site.register(Bread, BreadAdmin)
admin.site.register(Cake, CakeAdmin)
admin.site.register(SemiFinishedProducts, SemiFinishedAdmin)

admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
