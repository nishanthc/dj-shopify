from django.contrib.auth.models import User
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


class Customer(TimeStampedModel):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=30,
    )
    email = models.CharField(
        max_length=30,
    )
    address = models.CharField(
        max_length=30,
    )

    def __str__(self):
        return self.email


class Order(TimeStampedModel):
    id = models.CharField(
        primary_key=True,
        max_length=30
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=CASCADE,
        related_name="customer",
        null=True
    )

    admin_graphql_api_id = models.CharField(
        max_length=30
    )
    app_id = models.CharField(
        max_length=30
    )
    browser_ip = models.CharField(
        max_length=30,
        null=True
    )
    buyer_accepts_marketing = models.CharField(
        max_length=30,
        null=True
    )
    cancel_reason = models.CharField(
        max_length=30,
        null=True
    )
    cancelled_at = models.CharField(
        max_length=30,
        null=True
    )
    cart_token = models.CharField(
        max_length=30,
        null=True
    )
    checkout_id = models.CharField(
        max_length=30,
        null=True
    )
    checkout_token = models.CharField(
        max_length=30,
        null=True
    )
    closed_at = models.CharField(
        max_length=30,
        null=True
    )
    confirmed = models.CharField(
        max_length=30,
        null=True
    )
    contact_email = models.CharField(
        max_length=30,
        null=True
    )
    created_at = models.CharField(
        max_length=30,
        null=True
    )
    currency = models.CharField(
        max_length=30,
        null=True
    )
    customer_locale = models.CharField(
        max_length=30,
        null=True
    )
    device_id = models.CharField(
        max_length=30,
        null=True
    )
    discount_applications = models.CharField(
        max_length=30,
        null=True
    )
    discount_codes = models.CharField(
        max_length=30,
        null=True
    )
    email = models.CharField(
        max_length=30,
        null=True
    )
    financial_status = models.CharField(
        max_length=30,
        null=True
    )
    fulfillment_status = models.CharField(
        max_length=30,
        null=True
    )
    fulfillments = models.CharField(
        max_length=30,
        null=True
    )
    gateway = models.CharField(
        max_length=30,
        null=True
    )
    landing_site = models.CharField(
        max_length=30,
        null=True
    )
    landing_site_ref = models.CharField(
        max_length=30,
        null=True
    )
    location_id = models.CharField(
        max_length=30,
        null=True
    )
    name = models.CharField(
        max_length=30,
        null=True
    )
    note = models.CharField(
        max_length=30,
        null=True
    )
    note_attributes = models.CharField(
        max_length=30,
        null=True
    )
    number = models.CharField(
        max_length=30,
        null=True
    )
    order_number = models.CharField(
        max_length=30,
        null=True
    )
    order_status_url = models.CharField(
        max_length=30,
        null=True
    )
    payment_gateway_names = models.CharField(
        max_length=30,
        null=True
    )
    phone = models.CharField(
        max_length=30,
        null=True
    )
    presentment_currency = models.CharField(
        max_length=30,
        null=True
    )
    processed_at = models.CharField(
        max_length=30,
        null=True
    )
    processing_method = models.CharField(
        max_length=30,
        null=True
    )
    reference = models.CharField(
        max_length=30,
        null=True
    )
    referring_site = models.CharField(
        max_length=30,
        null=True
    )
    refunds = models.CharField(
        max_length=30,
        null=True
    )
    shipping_lines = models.CharField(
        max_length=30,
        null=True
    )
    source_identifier = models.CharField(
        max_length=30,
        null=True
    )
    source_name = models.CharField(
        max_length=30,
        null=True
    )
    source_url = models.CharField(
        max_length=30,
        null=True
    )
    subtotal_price = models.CharField(
        max_length=30,
        null=True
    )
    subtotal_price_set = models.CharField(
        max_length=30,
        null=True
    )
    tags = models.CharField(
        max_length=30,
        null=True
    )
    tax_lines = models.CharField(
        max_length=30,
        null=True
    )
    taxes_included = models.CharField(
        max_length=30,
        null=True
    )
    test = models.CharField(
        max_length=30,
        null=True
    )
    token = models.CharField(
        max_length=30,
        null=True
    )
    test = models.CharField(
        max_length=30,
        null=True
    )

    line_items = models.CharField(
        max_length=100,
        null=True
    )
    total_discounts = models.CharField(
        max_length=30,
        null=True
    )
    total_discounts_set = models.CharField(
        max_length=30,
        null=True
    )
    total_line_items_price = models.CharField(
        max_length=30,
        null=True
    )
    total_line_items_price_set = models.CharField(
        max_length=30,
        null=True
    )
    total_price = models.CharField(
        max_length=30,
        null=True
    )
    total_price_set = models.CharField(
        max_length=30,
        null=True
    )
    total_price_usd = models.CharField(
        max_length=30,
        null=True
    )
    total_shipping_price_set = models.CharField(
        max_length=30,
        null=True
    )
    total_tax = models.CharField(
        max_length=30,
        null=True
    )
    total_tax_set = models.CharField(
        max_length=30,
        null=True
    )
    total_tip_received = models.CharField(
        max_length=30,
        null=True
    )
    total_weight = models.CharField(
        max_length=30,
        null=True
    )
    updated_at = models.CharField(
        max_length=30,
        null=True
    )
    user_id = models.CharField(
        max_length=30,
        null=True
    )

    def __str__(self):
        return self.name
