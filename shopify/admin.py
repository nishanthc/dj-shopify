from django.contrib import admin

# Register your models here.
from shopify.models import Product, Variant


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class VariantAdmin(admin.ModelAdmin):
    pass


admin.site.register(Variant, VariantAdmin)
