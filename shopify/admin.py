from django.contrib import admin

# Register your models here.
from shopify.models import Product


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
