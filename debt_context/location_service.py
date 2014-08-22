from debt_context.models import CityDebt, CountyDebt, SchoolDistrictDebt


class LocationService(object):
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def __call__(self):
        return [
            CityDebt.objects.get(id=1),
            CountyDebt.objects.get(id=1),
            SchoolDistrictDebt.objects.get(id=1)
        ]
