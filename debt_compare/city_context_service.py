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
        output = []

        if 'up' in context and context['up'].id != self.city.id:
            output.append(context['up'].to_short_dict())

        output.append(self.city.to_short_dict())

        if 'down' in context and context['down'].id != self.city.id:
            output.append(context['down'].to_short_dict())

        # If there is no context, will return an empty Array
        if len(output) == 1:
            return []
        else:
            return output

    def context_population(self):
        output = {}
        population = self.city.population
        if population == None:
            return output

        output['up'] = CityDebt.objects.filter(population__gt=population).\
            order_by('population').first()
        output['down'] = CityDebt.objects.filter(population__lt=population).\
            order_by('-population').first()

        return output

    def context_tax_debt_per_capita(self):
        output = {}
        tax_debt_per_capita = self.city.tax_debt_per_capita
        if tax_debt_per_capita == None:
            return output

        up = CityDebt.objects.filter(tax_debt_per_capita__gt=tax_debt_per_capita).\
            order_by('tax_debt_per_capita').first()
        down = CityDebt.objects.filter(tax_debt_per_capita__lt=tax_debt_per_capita).\
            order_by('-tax_debt_per_capita').first()

        if up:
            output['up'] = up

        if down:
            output['down'] = down

        return output

    def context_tax_debt_to_assessed_valuation(self):
        output = {}
        tax_debt_to_assessed_valuation = self.city.tax_debt_to_assessed_valuation
        if tax_debt_to_assessed_valuation == None:
            return output

        up = CityDebt.objects.filter(tax_debt_to_assessed_valuation__gt=tax_debt_to_assessed_valuation).order_by('tax_debt_to_assessed_valuation').first()
        down = CityDebt.objects.filter(tax_debt_to_assessed_valuation__lt=tax_debt_to_assessed_valuation).order_by('-tax_debt_to_assessed_valuation').first()

        return { 'up': up, 'down': down }
