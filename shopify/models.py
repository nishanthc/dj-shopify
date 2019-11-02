from django.db import models

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
