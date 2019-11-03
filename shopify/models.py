from django.db import models
from django.db.models import CASCADE

from model_utils.models import TimeStampedModel


class Product(TimeStampedModel):
    id = models.CharField(
        primary_key=True,
        max_length=30
    )
    title = models.CharField(
        max_length=30
    )
    body_html = models.CharField(
        max_length=30
    )
    vendor = models.CharField(
        max_length=30
    )
    product_type = models.CharField(
        max_length=30
    )
    created_at = models.CharField(
        max_length=30
    )
    handle = models.CharField(
        max_length=30
    )
    updated_at = models.CharField(
        max_length=30
    )
    published_at = models.CharField(
        max_length=30
    )
    template_suffix = models.CharField(
        max_length=30
    )
    tags = models.CharField(
        max_length=30
    )
    published_scope = models.CharField(
        max_length=30
    )
    admin_graphql_api_id = models.CharField(
        max_length=30
    )
    image = models.CharField(
        max_length=30,
        null=True
    )

    def __str__(self):
        return self.title


class Variant(TimeStampedModel):
    id = models.CharField(
        primary_key=True,
        max_length=30
    )
    admin_graphql_api_id = models.CharField(
        max_length=30
    )
    barcode = models.CharField(
        max_length=30
    )
    compare_at_price = models.CharField(
        max_length=30,
        null=True
    )
    created_at = models.CharField(
        max_length=30
    )
    fulfillment_service = models.CharField(
        max_length=30
    )
    grams = models.CharField(
        max_length=30
    )
    image_id = models.CharField(
        max_length=30,
        null=True

    )
    inventory_item_id = models.CharField(
        max_length=30
    )
    inventory_management = models.CharField(
        max_length=30
    )
    inventory_policy = models.CharField(
        max_length=30
    )
    inventory_quantity = models.CharField(
        max_length=30
    )
    old_inventory_quantity = models.CharField(
        max_length=30
    )
    option1 = models.CharField(
        max_length=30
    )
    option2 = models.CharField(
        max_length=30,
        null=True

    )
    option3 = models.CharField(
        max_length=30,
        null=True

    )
    position = models.CharField(
        max_length=30
    )
    price = models.CharField(
        max_length=30
    )
    product_id = models.ForeignKey(Product, on_delete=CASCADE, related_name="variants")
    requires_shipping = models.CharField(
        max_length=30
    )
    sku = models.CharField(
        max_length=30
    )
    taxable = models.CharField(
        max_length=30
    )
    title = models.CharField(
        max_length=30
    )
    updated_at = models.CharField(
        max_length=30
    )
    weight = models.CharField(
        max_length=30
    )
    weight_unit = models.CharField(
        max_length=30
    )

    def __str__(self):
        return f"{self.product_id} - {self.title}"


class Order(TimeStampedModel):
    id = models.CharField(
        primary_key=True,
        max_length=30
    )
    admin_graphql_api_id = models.CharField(
        max_length=30
    )
    app_id = models.CharField(
        max_length=30
    )
    browser_id = models.CharField(
        max_length=30
    )
    buyer_accepts_marketing = models.CharField(
        max_length=30
    )
    cancel_reason = models.CharField(
        max_length=30
    )
    cancelled_at = models.CharField(
        max_length=30
    )
    cart_token = models.CharField(
        max_length=30
    )
    checkout_id = models.CharField(
        max_length=30
    )
    checkout_token = models.CharField(
        max_length=30
    )
    closed_at = models.CharField(
        max_length=30
    )
    confirmed = models.CharField(
        max_length=30
    )
    contact_email = models.CharField(
        max_length=30
    )
    created_at = models.CharField(
        max_length=30
    )
    currency = models.CharField(
        max_length=30
    )
    customer_locale = models.CharField(
        max_length=30
    )
    device_id = models.CharField(
        max_length=30
    )
    discount_applications = models.CharField(
        max_length=30
    )
    discount_codes = models.CharField(
        max_length=30
    )
    email = models.CharField(
        max_length=30
    )
    financial_status = models.CharField(
        max_length=30
    )
    fulfillment_status = models.CharField(
        max_length=30
    )
    fulfillments = models.CharField(
        max_length=30
    )
    gateway = models.CharField(
        max_length=30
    )
    landing_site = models.CharField(
        max_length=30
    )
    landing_site_ref = models.CharField(
        max_length=30
    )
    location_id = models.CharField(
        max_length=30
    )
    name = models.CharField(
        max_length=30
    )
    note = models.CharField(
        max_length=30
    )
    note_attributes = models.CharField(
        max_length=30
    )
    number = models.CharField(
        max_length=30
    )
    order_number = models.CharField(
        max_length=30
    )
    order_status_url = models.CharField(
        max_length=30
    )
    payment_gateway_names = models.CharField(
        max_length=30
    )
    phone = models.CharField(
        max_length=30
    )
    presentment_currency = models.CharField(
        max_length=30
    )
    processed_at = models.CharField(
        max_length=30
    )
    processing_method = models.CharField(
        max_length=30
    )
    reference = models.CharField(
        max_length=30
    )
    referring_site = models.CharField(
        max_length=30
    )
    refunds = models.CharField(
        max_length=30
    )
    shipping_lines = models.CharField(
        max_length=30
    )
    source_identifier = models.CharField(
        max_length=30
    )
    source_name = models.CharField(
        max_length=30
    )
    source_url = models.CharField(
        max_length=30
    )
    subtotal_price = models.CharField(
        max_length=30
    )
    subtotal_price_set = models.CharField(
        max_length=30
    )
    tags = models.CharField(
        max_length=30
    )
    tax_lines = models.CharField(
        max_length=30
    )
    taxes_included = models.CharField(
        max_length=30
    )
    test = models.CharField(
        max_length=30
    )
