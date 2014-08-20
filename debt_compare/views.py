import json
from django.http import HttpResponse
from debt_compare.location_service import LocationService
from debt_compare.search_service import SearchService


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

    city, county, ids = LocationService(lat=lat, lng=lng)()

    output = {
        'current': {
            'city': city.to_dict(),
            'county': county.to_dict(),
            'ids': ids.to_dict()
        }
    }

    return JsonpResponse(json.dumps(output), request=request)


def search(request):
    city, county, ids = SearchService(query=request.GET['q'])()

    output = {
        'current': {
            'city': city.to_dict(),
            'county': county.to_dict(),
            'ids': ids.to_dict()
        }
    }

    return JsonpResponse(json.dumps(output), request=request)
