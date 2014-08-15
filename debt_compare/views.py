import json
from django.http import HttpResponse
from debt_compare.county_compare_service import CountyCompareService


def index(request):
    city_id = request.GET['city_id']
    return HttpResponse(json.dumps(CountyCompareService(city_id)()), content_type="application/json")
