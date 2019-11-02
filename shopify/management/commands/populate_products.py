from django.core.management.base import BaseCommand, CommandError

from shopify.api.api import populate_products


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        populate_products()