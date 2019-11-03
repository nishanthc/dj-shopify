from pprint import pprint
import json
import requests

from djshopify.settings import SHOPIFY_URL
from shopify.models import Product, Variant, Order


def create_order(customer, cart_items):
    line_items = []

    for item in cart_items:
        line = {
            "variant_id": item.id,
            "quantity": 1
        }
        line_items.append(line)
    data = {
        "order": {
            "inventory_behaviour":"decrement_obeying_policy",
            "fulfillment_status": "fulfilled",
            "line_items": line_items,
            "customer": {
                "first_name": customer.first_name,
                "last_name": customer.last_name,
                "email": customer.email
            },
            "financial_status": "paid",
            "shipping_address": {
                "first_name": customer.first_name,
                "last_name": customer.last_name,
                "address1": customer.address,

            },
            "billing_address": {
                "first_name": customer.first_name,
                "last_name": customer.last_name,
                "address1": customer.address,

            }
        }
    }
    x = requests.post(SHOPIFY_URL + 'orders.json', json=data)
    order_id = json.loads(x.content)["order"]["id"]
    populate_products()
    populate_orders()
    if customer:
        customer.save()
        order = Order.objects.get(id=order_id)
        order.customer = customer
        order.save()


def populate_products():
    response = requests.get(SHOPIFY_URL + 'products.json')
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
    response = requests.get(SHOPIFY_URL + 'orders.json' + '?status=any')
    response_dictionary = json.loads(response.content)
    orders = response_dictionary["orders"]

    for order in orders:
        order_object, created = Order.objects.update_or_create(
            id=order["id"],
            defaults={
                "admin_graphql_api_id": order["admin_graphql_api_id"],
                "app_id": order["app_id"],
                "browser_ip": order["browser_ip"],
                "buyer_accepts_marketing": order["buyer_accepts_marketing"],
                "cancel_reason": order["cancel_reason"],
                "cancelled_at": order["cancelled_at"],
                "cart_token": order["cart_token"],
                "checkout_id": order["checkout_id"],
                "checkout_token": order["checkout_token"],
                "closed_at": order["closed_at"],
                "confirmed": order["confirmed"],
                "contact_email": order["contact_email"],
                "created_at": order["created_at"],
                "currency": order["currency"],
                "customer_locale": order["customer_locale"],
                "device_id": order["device_id"],
                "discount_applications": order["discount_applications"],
                "discount_codes": order["discount_codes"],
                "email": order["email"],
                "financial_status": order["financial_status"],
                "fulfillment_status": order["fulfillment_status"],
                "fulfillments": order["fulfillments"],
                "gateway": order["gateway"],
                "landing_site": order["landing_site"],
                "landing_site_ref": order["landing_site_ref"],
                "line_items": order["line_items"],
                "location_id": order["location_id"],
                "name": order["name"],
                "note": order["note"],
                "note_attributes": order["note_attributes"],
                "number": order["number"],
                "order_number": order["order_number"],
                "order_status_url": order["order_status_url"],
                "payment_gateway_names": order["payment_gateway_names"],
                "phone": order["phone"],
                "presentment_currency": order["presentment_currency"],
                "processed_at": order["processed_at"],
                "processing_method": order["processing_method"],
                "reference": order["reference"],
                "refunds": order["refunds"],
                "referring_site": order["referring_site"],
                "shipping_lines": order["shipping_lines"],
                "source_identifier": order["source_identifier"],
                "source_name": order["source_name"],
                "source_url": order["source_url"],
                "subtotal_price": order["subtotal_price"],
                "subtotal_price_set": order["subtotal_price_set"],
                "tags": order["tags"],
                "tax_lines": order["tax_lines"],
                "taxes_included": order["taxes_included"],
                "test": order["test"],
                "token": order["token"],
                "total_discounts": order["total_discounts"],
                "total_discounts_set": order["total_discounts_set"],
                "total_line_items_price": order["total_line_items_price"],
                "total_line_items_price_set": order["total_line_items_price_set"],
                "total_price": order["total_price"],
                "total_price_set": order["total_price_set"],
                "total_price_usd": order["total_price_usd"],
                "total_shipping_price_set": order["total_shipping_price_set"],
                "total_tax": order["total_tax"],
                "total_tax_set": order["total_tax_set"],
                "total_tip_received": order["total_tip_received"],
                "updated_at": order["updated_at"],
                "user_id": order["user_id"],

            }
        )
