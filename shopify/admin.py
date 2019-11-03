from django.contrib import admin

# Register your models here.
from shopify.models import Product, Variant, Order, Customer


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class VariantAdmin(admin.ModelAdmin):
    pass


admin.site.register(Variant, VariantAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)

class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)

from django.contrib.sessions.models import Session


class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()

    list_display = ['session_key', '_session_data', 'expire_date']


admin.site.register(Session, SessionAdmin)
