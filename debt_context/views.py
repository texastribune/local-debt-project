import json

from django.http import HttpResponse

from debt_context.services.search_service import SearchService
from debt_context.services.context_service import ContextService


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


def search(request):
    search_service = SearchService(query=request.GET['q'])
    status = search_service.status()
    issuers = search_service.issuers()
    issuers.sort()

    output = {
        'issuers': [],
        'meta': {
            'q': request.GET['q'],
            'status': status['status'],
            'display_name': status['display_name']
        }
    }

    for issuer in issuers:
        output['issuers'].append(
            {
                'current': issuer.to_dict(),
                'context': ContextService(issuer).context()
            }
        )

    return JsonpResponse(json.dumps(output), request=request)
