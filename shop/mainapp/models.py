from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Category
# Product
# CartProduct
# Cart
# Order

# Customer
# Specification

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Categoty name")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Product name")
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name="Image")
    description = models.TextField(verbose_name="Description", null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Price")

    def __str__(self):
        return self.title


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name="Customer", on_delete=models.CASCADE)
    cart = models.ForeignKey("Cart", verbose_name="Cart", on_delete=models.CASCADE, related_name="related_products")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Total price")

    def __str__(self):
        return f"Cart Item: {self.title}"


class Bakery(Product):
    ingredients = models.TextField(verbose_name="Ingredients", null=True)
    allergens = models.CharField(max_length=255, verbose_name='Allergens')

    def __str__(self):
        return f"{self.category.name} : {self.title}"


class Cake(Product):
    ingredients = models.TextField(verbose_name="Ingredients", null=True)
    allergens = models.CharField(max_length=255, verbose_name='Allergens')
    weight = models.CharField(max_length=255, verbose_name='Weight')

    def __str__(self):
        return f"{self.category.name} : {self.title}"


class Cart(models.Model):
    owner = models.ForeignKey("Customer", verbose_name="Owner", on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name="related_cart")
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Total price")

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name="Phone number")
    adress = models.CharField(max_length=255, verbose_name="Adress")
    email = models.EmailField(max_length=255, verbose_name='Email')
    birthday = models.DateField(help_text = "Customer birthdate", verbose_name='Birthday')

    def __str__(self):
        return f"User: {self.user.first_name} {self.user.last_name}"
