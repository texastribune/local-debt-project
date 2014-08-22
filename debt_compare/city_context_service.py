from debt_compare.models import CityDebt


class CityContextService(object):
    def __init__(self, city):
        self.city = city

    def population_context(self):
        return self.hashify(self.context_population())

    def tax_debt_to_assessed_valuation(self):
        return self.hashify(self.context_tax_debt_to_assessed_valuation())

    def tax_debt_per_capita(self):
        return self.hashify(self.context_tax_debt_per_capita())

    def hashify(self, context):
        # If there is no context, will return an empty Array
        if len(context) == 1:
            return []
        else:
            return [entity.to_short_dict() for entity in context]

    def context_population(self):
        output = []
        population = self.city.population

        if population == None:
            return [self.city]

        output = output + list(CityDebt.objects.filter(population__gt=population).\
            order_by('population')[:2])

        output.append(self.city)
        output = output + list(CityDebt.objects.filter(population__lt=population).\
            order_by('-population')[:2])

        return output

    def context_tax_debt_per_capita(self):
        output = []
        tax_debt_per_capita = self.city.tax_debt_per_capita

        if tax_debt_per_capita == None:
            return [self.city]

        output = output + list(CityDebt.objects.filter(tax_debt_per_capita__gt=\
            tax_debt_per_capita).order_by('tax_debt_per_capita')[:2])

        output.append(self.city)
        output = output + list(CityDebt.objects.filter(tax_debt_per_capita__gt=\
            tax_debt_per_capita).order_by('-tax_debt_per_capita')[:2])

        return output

    def context_tax_debt_to_assessed_valuation(self):
        output = []
        tax_debt_to_assessed_valuation = self.city.tax_debt_to_assessed_valuation
        if tax_debt_to_assessed_valuation == None:
            return [self.city]

        output = output + list(CityDebt.objects.filter(tax_debt_to_assessed_valuation__gt=\
            tax_debt_to_assessed_valuation).order_by('tax_debt_to_assessed_valuation')[:2])

        output.append(self.city)
        output = output + list(CityDebt.objects.filter(tax_debt_to_assessed_valuation__gt=\
            tax_debt_to_assessed_valuation).order_by('-tax_debt_to_assessed_valuation')[:2])

        return output
