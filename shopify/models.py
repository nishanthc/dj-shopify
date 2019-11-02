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
    product_id = models.ForeignKey(Product, on_delete=CASCADE)
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
