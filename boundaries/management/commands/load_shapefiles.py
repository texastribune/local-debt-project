import os
import sys

from django.conf import settings
from django.contrib.gis.utils import LayerMapping
from django.core.management.base import BaseCommand

from boundaries.models import Collection, Shape

SHAPEFILES_DIR = 'boundaries/data/shapefiles'


class Command(BaseCommand):
    help = "Import all shapefiles."

    def handle(self, *args, **options):
        sys.path.append(os.path.join(settings.SITE_DIR, SHAPEFILES_DIR))
        from definitions import SHAPEFILES

        for name, options in SHAPEFILES.items():
            self.stdout.write('Processing \'{}\' now...'.format(name))

            self.stdout.write('Attempting to create collection...')
            collection, _ = Collection.objects.get_or_create(
                name=name,
                authority=options['authority'],
                last_updated=options['last_updated'],
                count=0,
                slug=options['slug'],
                source_url=options['source_url']
            )

            if _ is True:
                self.stdout.write('\'{}\' collection created!'.format(name))
            else:
                self.stdout.write('\'{}\' collection already exists!'
                                  ' Not a problem.'.format(name))

            lm = LayerMapping(Shape,
                              os.path.join(SHAPEFILES_DIR, options['file']),
                              options['layer_mapping'],
                              encoding='latin-1')

            lm.save(verbose=True, strict=True)
