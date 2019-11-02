# Create your views here.
from pprint import pprint

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, RedirectView

from shopify.models import Product, Variant


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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = super(ProductDetailView, self).get_object()
        context["variants"] = product.variants.all()
        pprint(context)

        return context


class AddToCartView(View):
    def get(self, *args, **kwargs):
        variant = get_object_or_404(Variant, pk=kwargs['pk'])
        if not self.request.user.is_authenticated:
            if self.request.session.is_empty():
                self.request.session['variants'] = []
            self.request.session['variants'].append(variant.id)
            messages.success(self.request, 'Product sucessfully added to your cart!')
            return redirect('product-detail', pk=variant.product_id.id)
        else:
            return redirect('product-detail', pk=variant.product_id.id)


