from pprint import pprint
import json
import requests

from djshopify.settings import SHOPIFY_URL
from shopify.models import Product


def populate_products():
    response = requests.get(SHOPIFY_URL)
    response_dictionary = json.loads(response.content)
    products = response_dictionary["products"]
    print(len(products))
    pprint(products)
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

