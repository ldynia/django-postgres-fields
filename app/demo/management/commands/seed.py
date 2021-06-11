from django.core.management.base import BaseCommand
from itertools import islice

from demo.models import Product
from config.base import SEED_SIZE


class Command(BaseCommand):

    def handle(self, *args, **options):
        batch_size = 10000

        objs = (
            Product(
                name=f'P-{i}',
                attributes={"name": i, "values": [i, i+1]},
            ) for i in range(SEED_SIZE)
        )

        while True:
            batch = list(islice(objs, batch_size))
            if not batch:
                break
            Product.objects.bulk_create(batch, batch_size)