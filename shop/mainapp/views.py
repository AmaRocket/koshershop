from django.shortcuts import render
from django.views.generic import DetailView

from .models import Bakery, Bread, Cake, SemiFinishedProducts, Category


# Create your views here.

def test_view(request):
    categories = Category.objects.get_categoryes_for_left_sidebar()
    return render(request, 'base.html', {"categories": categories})


class ProductDetailView(DetailView):
    CT_MODEL_MODEL_CLASS = {
        "bakery": Bakery,
        "bread": Bread,
        "cake": Cake,
        "semifinishedproducts": SemiFinishedProducts
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs["ct_model"]]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = "product"
    template_name = "product_detail.html"
    slug_url_kwarg = "slug"
