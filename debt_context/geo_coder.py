import json
import random
import urllib
import urllib2


class GeoCoder(object):
    def __init__(self, query):
        self.query = query

    def __call__(self):
        try:
            parsed_response = json.loads(urllib2.urlopen(self.build_url()).read())

            if parsed_response[0]['address']['state'] != 'Texas':
                return self.random_place()
            else:
                return {
                    'status': 'ok',
                    'display_name': parsed_response[0]['display_name'],
                    'lat': parsed_response[0]['lat'],
                    'lng': parsed_response[0]['lat']
                }

        except (urllib2.URLError, urllib2.HTTPError, ValueError, KeyError, IndexError), e:
            return self.random_place()


    def build_url(self):
        base = "http://open.mapquestapi.com/nominatim/v1/search.php"
        options = {
            'format': 'json',
            'countrycodes': 'us',
            'limit': 1,
            'addressdetails': 1,
            'q': self.query
        }
        query_string = urllib.urlencode(options)
        return base + '?' + query_string

    def random_place(self):
        places = [
            {
                'status': 'error',
                'display_name': 'Austin, Travis County',
                'lat': '30.2711286',
                'lng': '-97.7436995'
            },
            {
                'status': 'error',
                'display_name': 'Dallas, Dallas County',
                'lat': '32.7761963',
                'lng': '-96.7968994',
            },
            {
                'status': 'error',
                'display_name': 'Houston, Harris County',
                'lat': '29.974286',
                'lng': '-95.5266759583333'
            },
            {
                'status': 'error',
                'display_name': 'San Antonio, Bexar County',
                'lat': '29.4246002',
                'lng': '-98.4951405'
            },
            {
                'status': 'error',
                'display_name': 'El Paso, El Paso County',
                'lat': '31.7600372',
                'lng': '-106.487287'
            }
        ]
        return random.choice(places)
