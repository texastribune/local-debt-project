class ContextualizerService(object):
    contextualizers = [
        CityContextService,
        CountyContextService,
        ISDContextService
    ]

    def __init__(self, issuers):
        self.issuers = issuers

    def __call__(self):
        for issuer in self.issuers:

