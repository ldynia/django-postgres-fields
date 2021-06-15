from django.core.management.base import BaseCommand
from itertools import islice

from demo.models import Product
from config.base import SEED_SIZE


class Command(BaseCommand):

    def handle(self, *args, **options):
        batch_size = 100000

        objs = (
            Product(
                name=str(i),
                name_idx=str(i),
                attributes={"name": str(i), 'number': i, "values": [i, i+1]},
                attributes_idx={"name": str(i), 'number': i, "values": [i, i+1]},
            ) for i in range(1, SEED_SIZE+1)
        )

        print("Seeding started")
        while True:
            batch = list(islice(objs, batch_size))
            if not batch:
                break
            Product.objects.bulk_create(batch, batch_size)
        print("Seeding stopped")