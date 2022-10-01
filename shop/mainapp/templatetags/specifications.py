from django import template
from django.utils.safestring import mark_safe
from mainapp.models import Bakery, Bread, Cake, SemiFinishedProducts

register = template.Library()

TABLE_HEAD = """
            <table class="table">
            <tbody>
            """

TABLE_CONTENT = """
            <tr>
            <td>{name}</td>
            <td>{value}</td>
            </tr>
                """

TABLE_TAIL = """
            </tbody>
            </table>
            """

PRODUCT_SPEC = {
    "bakery": {
        "Ingredients": "ingredients",
        "Allergens": "allergens",
        "Allergens volume": "allergens_volume"
    },
    "bread": {
        "Ingredients": "ingredients",
        "Allergens": "allergens",
        "Allergens volume": "allergens_volume"
    },
    "cake": {
        "Ingredients": "ingredients",
        "Allergens": "allergens",
        "Allergens volume": "allergens_volume",
        "Weight": "weight"
    },
    "semifinishedproducts": {
        "Ingredients": "ingredients",
        "Allergens": "allergens",
        "Allergens volume": "allergens_volume",
        "Weight": "weight"
    }

}

def get_product_spec(product, model_name):
    table_content = ""
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    if isinstance(product, Bakery):
        if not product.allergens:
            PRODUCT_SPEC.pop("Allergens volume", None)
        else:
            PRODUCT_SPEC["bakery"]["Allergens volume"] =  "allergens_volume"

    elif isinstance(product, Bread):
        if not product.allergens:
            PRODUCT_SPEC["bread"].pop("Allergens volume", None)
        else:
            PRODUCT_SPEC["bread"]["Allergens volume"] = 'allergens_volume'

    elif isinstance(product, Cake):
        if not product.allergens:
            PRODUCT_SPEC["cake"].pop("Allergens volume", None)
        else:
            PRODUCT_SPEC["cake"]["Allergens volume"] = 'allergens_volume'

    elif isinstance(product, SemiFinishedProducts):
        if not product.allergens:
            PRODUCT_SPEC["semifinishedproducts"].pop("Allergens volume", None)
        else:
            PRODUCT_SPEC["semifinishedproducts"]["Allergens volume"] = 'allergens_volume'

    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)
