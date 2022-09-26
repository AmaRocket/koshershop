from django import forms
from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm

from .models import *
from PIL import Image

class CakeAdminForm(ModelForm):

    MIN_RESOLUTION = (600, 600)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = f"Upload images with min resolution {self.MIN_RESOLUTION[0]} x {self.MIN_RESOLUTION[1]}"

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = self.MIN_RESOLUTION

        return image


class CakeAdmin(admin.ModelAdmin):

    form = CakeAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='Cake'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class BaketyAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='Bakery'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)

admin.site.register(Bakery, BaketyAdmin)
admin.site.register(Cake, CakeAdmin)

admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
