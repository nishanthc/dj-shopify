# Create your views here.
from pprint import pprint

from django.views.generic import TemplateView, ListView

from shopify.models import Product


class ProductListingView(ListView):
    model = Product
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pprint(context)
        return context

class CartView(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_items"] = "test"
        pprint(context)
        return context
