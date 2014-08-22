import json
from django.http import HttpResponse
from debt_context.location_service import LocationService
from debt_context.search_service import SearchService
from debt_context.city_context_service import CityContextService
from debt_context.county_context_service import CountyContextService
# from debt_compare.isd_context_service import ISDContextService


class JsonpResponse(HttpResponse):
    """
    Wrapper that sets the mimetype and adds a callback if necessary.
    Usage: use this just like HttpResponse, but make sure you pass in content
    and the request.
    """
    def __init__(self, content, request, mimetype='application/json',
        *args, **kwargs):
        callback = request.GET.get('callback')
        if callback:
            content = '{0}({1})'.format(callback, content)
            mimetype = 'application/javascript'
        super(JsonpResponse, self).__init__(content, mimetype, *args, **kwargs)


def location(request):
    lat = request.GET['lat']
    lng =  request.GET['lng']

    city, county, isd = LocationService(lat=lat, lng=lng)()

    output = {
        'current': {
            'city': city.to_dict(),
            'county': county.to_dict(),
            'isd': isd.to_dict()
        }
    }

    return JsonpResponse(json.dumps(output), request=request)


def search(request):
    city, county, isd = SearchService(query=request.GET['q'])()
    city_context_service = CityContextService(city)
    county_context_service = CountyContextService(county)

    output = {
        'current': {
            'city': city.to_dict(),
            'county': county.to_dict(),
            'isd': isd.to_dict()
        },
        'population': {
            'city': city_context_service.population_context(),
            'county': county_context_service.population_context()
        },
        'debtToAssessedValuation': {
            'city': city_context_service.tax_debt_to_assessed_valuation(),
            'county': county_context_service.tax_debt_to_assessed_valuation()
        },
        'taxtDebtPerCapita': {
            'city': city_context_service.tax_debt_per_capita(),
            'county': county_context_service.tax_debt_per_capita()
        }
    }

    # return JsonpResponse(json.dumps(output), request=request)
    return HttpResponse(json.dumps(output), 'application/json')
