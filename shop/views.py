# Create your views here.
from pprint import pprint

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, RedirectView, CreateView

from shopify.api.api import create_order
from shopify.models import Product, Variant, Customer


class ProductListingView(ListView):
    model = Product
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pprint(context)
        return context


class CartView(CreateView):
    model = Customer
    fields = ('first_name', 'last_name', 'address','email')
    success_url = "success"
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        variants_list = []

        if not self.request.user.is_authenticated:
            variants_session = self.request.session['variants']
            for variant in variants_session:
                try:
                    variant_object = Variant.objects.get(id=variant)
                    variants_list.append(variant_object)
                except Variant.DoesNotExist:
                    pass
        total = 0
        for variant in variants_list:
            total = total + float(variant.price)
        context["cart_items"] = variants_list
        context["total"] = total
        return context

    def form_valid(self, form, **kwargs):
        if self.request.user:
            user = self.request.user

            form.instance.user = user.id
        context = self.get_context_data(**kwargs)
        cart_items = context["cart_items"]
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        address = form.cleaned_data['address']
        email = form.cleaned_data['email']
        customer = form.instance
        create_order(customer,cart_items)
        self.request.session['variants'] = []

        return super().form_valid(form)


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

class RemoveFromCartView(View):
    def get(self, *args, **kwargs):
        variant = get_object_or_404(Variant, pk=kwargs['pk'])
        if not self.request.user.is_authenticated:
            self.request.session['variants'].remove(variant.id)
            messages.success(self.request, 'Product removed from your cart!')
            return redirect('cart')
        else:
            return redirect('cart')
