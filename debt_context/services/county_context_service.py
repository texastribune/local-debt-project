from debt_context.services.context_base import ContextBase
from debt_context.models import CountyDebt


class CountyContextService(ContextBase):
    def __init__(self, county):
        self.county = county

    def context_population(self):
        output = []
        population = self.county.population

        if population == None:
            return [self.county]

        output = output + list(CountyDebt.objects.filter(population__gt=population).\
            order_by('population')[:2])

        output.append(self.county)
        output = output + list(CountyDebt.objects.filter(population__lt=population).\
            order_by('-population')[:2])

        return output

    def context_tax_debt_per_capita(self):
        output = []
        tax_debt_per_capita = self.county.tax_debt_per_capita

        if tax_debt_per_capita == None:
            return [self.county]

        output = output + list(CountyDebt.objects.filter(tax_debt_per_capita__gt=tax_debt_per_capita).\
            order_by('tax_debt_per_capita')[:2])

        output.append(self.county)
        output = output + list(CountyDebt.objects.filter(tax_debt_per_capita__gt=tax_debt_per_capita).\
            order_by('-tax_debt_per_capita')[:2])

        return output

    def context_assessed_valuation(self):
        output = []
        tax_year_valuation = self.county.tax_year_valuation
        if tax_year_valuation == None:
            return [self.county]

        output = output + list(CountyDebt.objects.filter(tax_year_valuation__gt=tax_year_valuation).\
            order_by('tax_year_valuation')[:2])

        output.append(self.county)
        output = output + list(CountyDebt.objects.filter(tax_year_valuation__lt=tax_year_valuation).\
            order_by('-tax_year_valuation')[:2])

        return output
