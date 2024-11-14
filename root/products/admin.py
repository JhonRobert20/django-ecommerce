from django.contrib.admin import ModelAdmin, register

from products.models import Category, Product, ProductDetails


@register(Product)
class ProductAdmin(ModelAdmin):
    pass


@register(ProductDetails)
class ProductDetailsAdmin(ModelAdmin):
    pass


@register(Category)
class CategoryAdmin(ModelAdmin):
    pass
