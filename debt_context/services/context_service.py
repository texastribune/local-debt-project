from debt_context.models import CityDebt, CountyDebt, SchoolDistrictDebt
from debt_context.services.city_context_service import CityContextService
from debt_context.services.county_context_service import CountyContextService
from debt_context.services.isd_context_service import ISDContextService


class ContextService(object):
    def __init__(self, issuer):
        self.issuer = issuer
        self.city_context_service = CityContextService(issuer)
        self.county_context_service = CountyContextService(issuer)
        self.isd_context_service = ISDContextService(issuer)

    def context(self):
        if type(self.issuer) is CityDebt:
            return {
                'population': self.city_context_service.population_context(),
                'debtToAssessedValuation': self.city_context_service.tax_debt_to_assessed_valuation()
            }
        elif type(self.issuer) is CountyDebt:
            return {
                'population': self.county_context_service.population_context(),
                'debtToAssessedValuation': self.county_context_service.tax_debt_to_assessed_valuation()
            }
        elif type(self.issuer) is SchoolDistrictDebt:
            return {
                'students': self.isd_context_service.debt_similar_school_size(),
                'debtToAssessedValuation': self.isd_context_service.similar_assessed_valuation()
            }
