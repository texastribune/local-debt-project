from debt_compare.models import CityDebt


class CityCompareService(object):
    def __init__(self, city_id):
        self.city_id = city_id
        self.city = CityDebt.objects.get(id=city_id)

    def __call__(self):
        return {
            'current': self.city.to_dict(),
            'population': self.hashify(self.context_population()),
            'tax_debt_per_capita': self.hashify(self.context_tax_debt_per_capita()),
            'tax_debt_to_assessed_valuation': self.hashify(self.context_tax_debt_to_assessed_valuation())
        }

    def hashify(self, context):
        output = {}
        if context['up'] != None and context['up'].id != self.city.id:
            output['up'] = context['up'].to_dict()

        if context['down'] != None and context['down'].id != self.city.id:
            output['down'] = context['down'].to_dict()

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

        return { 'up': up, 'down': down }

    def context_tax_debt_to_assessed_valuation(self):
        output = {}
        tax_debt_to_assessed_valuation = self.city.tax_debt_to_assessed_valuation
        if tax_debt_to_assessed_valuation == None:
            return output

        up = CityDebt.objects.filter(tax_debt_to_assessed_valuation__gt=tax_debt_to_assessed_valuation).order_by('tax_debt_to_assessed_valuation').first()
        down = CityDebt.objects.filter(tax_debt_to_assessed_valuation__lt=tax_debt_to_assessed_valuation).order_by('-tax_debt_to_assessed_valuation').first()

        return { 'up': up, 'down': down }
