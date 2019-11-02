# Create your views here.

from django.views.generic import TemplateView


class ProductListingView(TemplateView):
    template_name = "product_listing.html"

    def dispatch(self, request, *args, **kwargs):
        return super(ProductListingView, self).dispatch(request, *args, **kwargs)