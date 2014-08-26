from django.contrib.gis.geos import Point
from debt_context.models import CityDebt, CountyDebt, SchoolDistrictDebt
from boundaries.models import Shape, Collection
from geo_coder import GeoCoder


class SearchService(object):
    def __init__(self, query):
        self.query = query
        self.geo_coder = GeoCoder(query)
        self._cache_geo_data = {}

    def issuers(self):
        pnt = Point(self.get_lng(), self.get_lat())
        shapes = Shape.objects.filter(shape__contains=pnt).order_by('collection')

        return filter(None, [self.load_issuer(shape) for shape in shapes])

    def geo_data(self):
        if 'status' not in self._cache_geo_data:
            self._cache_geo_data = self.geo_coder()
        return self._cache_geo_data

    def status(self):
        return {
            'status': self.geo_data()['status'],
            'display_name': self.geo_data()['display_name']
        }

    def get_lng(self):
        return float(self.geo_data()['lng'])

    def get_lat(self):
        return float(self.geo_data()['lat'])

    def load_issuer(self, shape):
        if shape.collection.name == 'Counties':
            return CountyDebt.objects.filter(shape=shape).first()
        elif shape.collection.name == 'Cities':
            return CityDebt.objects.filter(shape=shape).first()
        elif shape.collection.name == 'School Districts':
            return SchoolDistrictDebt.objects.filter(shape=shape).first()
