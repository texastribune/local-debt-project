from debt_context.models import CityDebt, CountyDebt, SchoolDistrictDebt


class SearchService(object):
    def __init__(self, query):
        self.query = query

    def __call__(self):
        return [
            CityDebt.objects.get(id=53),
            CountyDebt.objects.get(id=234),
            SchoolDistrictDebt.objects.get(id=1)
        ]
