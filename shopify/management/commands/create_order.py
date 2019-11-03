from django.core.management.base import BaseCommand, CommandError

from shopify.api.api import  create_order


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        create_order()