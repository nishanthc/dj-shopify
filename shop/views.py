# Create your views here.
import ast
from pprint import pprint

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, RedirectView, CreateView

from shopify.api.api import create_order
from shopify.models import Product, Variant, Customer, Order


class ProductListingView(ListView):
    model = Product
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class OrderListingView(ListView):
    model = Order
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class CustomerListingView(ListView):
    model = Customer
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class CartView(CreateView):
    model = Customer
    fields = ('first_name', 'last_name', 'address', 'email')
    success_url = "success"
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        variants_list = []
        if "variants" in self.request.session:
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
            if not user.id == None:
                form.instance.user = user
        context = self.get_context_data(**kwargs)
        cart_items = context["cart_items"]
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        address = form.cleaned_data['address']
        email = form.cleaned_data['email']
        customer = form.instance
        if create_order(customer, cart_items) == "error":
            messages.success(self.request, 'Error purchasing items!')
            return redirect('cart')
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


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = super(CustomerDetailView, self).get_object()
        context["orders"] = Order.objects.filter(customer=customer.id)
        pprint(context["orders"])

        return context


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = super(OrderDetailView, self).get_object()

        variants_with_price = []
        line_items = ast.literal_eval(order.line_items)
        for item in line_items:
            pprint(item)
            variants_with_price.append({
                "variant": Variant.objects.get(id=item["variant_id"]),
                "price": item["price"]
            })
        context["order_items"] = variants_with_price

        return context

class SuccessView(TemplateView):
    template_name = 'success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AddToCartView(View):
    def get(self, *args, **kwargs):
        variant = get_object_or_404(Variant, pk=kwargs['pk'])
        if not "variants" in self.request.session:
            self.request.session['variants'] = []
        self.request.session['variants'].append(variant.id)
        messages.success(self.request, 'Product sucessfully added to your cart!')
        return redirect('product-detail', pk=variant.product_id.id)


class RemoveFromCartView(View):
    def get(self, *args, **kwargs):
        variant = get_object_or_404(Variant, pk=kwargs['pk'])
        self.request.session['variants'].remove(variant.id)
        messages.success(self.request, 'Product removed from your cart!')
        return redirect('cart')
