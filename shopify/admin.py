from django.contrib import admin

# Register your models here.
from shopify.models import Product, Variant, Order


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class VariantAdmin(admin.ModelAdmin):
    pass


admin.site.register(Variant, VariantAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)

from django.contrib.sessions.models import Session


class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()

    list_display = ['session_key', '_session_data', 'expire_date']


admin.site.register(Session, SessionAdmin)
