from pprint import pprint
import json
import requests

from djshopify.settings import SHOPIFY_URL
from shopify.models import Product, Variant


def populate_products():
    response = requests.get(SHOPIFY_URL+'products.json')
    response_dictionary = json.loads(response.content)
    products = response_dictionary["products"]
    for product in products:
        product_object, created = Product.objects.update_or_create(
            id=product["id"],
            defaults={
                'title': product["title"],
                'body_html': product["body_html"],
                'vendor': product["vendor"],
                'product_type': product["product_type"],
                'created_at': product["created_at"],
                'handle': product["handle"],
                'updated_at': product["updated_at"],
                'published_at': product["published_at"],
                'template_suffix': product["template_suffix"],
                'tags': product["tags"],
                'published_scope': product["published_scope"],
                'admin_graphql_api_id': product["admin_graphql_api_id"],
                'image': product["image"]
            }
        )
        variants = product["variants"]
        for variant in variants:
            pprint(variant)
            variant_object, created = Variant.objects.update_or_create(
                id=variant["id"],
                defaults={
                    'admin_graphql_api_id': variant["admin_graphql_api_id"],
                    'barcode': variant["barcode"],
                    'compare_at_price': variant["compare_at_price"],
                    'created_at': variant["created_at"],
                    'fulfillment_service': variant["fulfillment_service"],
                    'grams': variant["grams"],
                    'image_id': variant["image_id"],
                    "inventory_item_id": variant["inventory_item_id"],
                    "inventory_management": variant["inventory_management"],
                    "inventory_policy": variant["inventory_policy"],
                    "inventory_quantity": variant["inventory_quantity"],
                    "old_inventory_quantity": variant["old_inventory_quantity"],
                    "option1": variant["option1"],
                    "option2": variant["option2"],
                    "option3": variant["option3"],
                    "position": variant["position"],
                    "price": variant["price"],
                    "product_id": product_object,
                    "requires_shipping": variant["requires_shipping"],
                    "sku": variant["sku"],
                    "taxable": variant["taxable"],
                    "title": variant["title"],
                    "updated_at": variant["updated_at"],
                    "weight": variant["weight"],
                    "weight_unit": variant["weight_unit"],

                }
            )

def populate_orders():
    response = requests.get(SHOPIFY_URL+'orders.json')
    response_dictionary = json.loads(response.content)
    orders = response_dictionary["orders"]

    for order in orders:
        pprint(order)
