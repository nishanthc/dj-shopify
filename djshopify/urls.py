"""djshopify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from shop.views import ProductListingView, CartView, ProductDetailView, AddToCartView, RemoveFromCartView, \
    OrderDetailView

urlpatterns = [
    path('', ProductListingView.as_view()),
    path('cart/', CartView.as_view(), name="cart"),
    re_path(r'^product/(?P<pk>\d+)$', ProductDetailView.as_view(), name='product-detail'),
    re_path(r'^add_to_cart/(?P<pk>\d+)$', AddToCartView.as_view(), name='add-to-cart'),
    re_path(r'^remove_from_cart/(?P<pk>\d+)$', RemoveFromCartView.as_view(), name='remove-from-cart'),
    re_path(r'^order/(?P<pk>\d+)$', OrderDetailView.as_view(), name='order-detail'),

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
