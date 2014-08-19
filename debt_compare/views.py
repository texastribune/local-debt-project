import json
from django.http import HttpResponse
from debt_compare.location_service import LocationService
from debt_compare.search_service import SearchService


def location(request):
    lat = request.GET['lat']
    lng =  request.GET['lng']

    city, county, ids = LocationService(lat=lat, lng=lng)()

    output = {
        'current': {
            'city': city.to_dict(),
            'county': county.to_dict(),
            'ids': ids.to_dict()
        }
    }

    return HttpResponse(json.dumps(output), content_type="application/json")

def search(request):
    city, county, ids = SearchService(query=request.GET['q'])()

    output = {
        'current': {
            'city': city.to_dict(),
            'county': county.to_dict(),
            'ids': ids.to_dict()
        }
    }

    return HttpResponse(json.dumps(output), content_type="application/json")
