from debt_context.context_base import ContextBase
from debt_context.models import SchoolDistrictDebt


class ISDContextService(ContextBase):
    def __init__(self, isd):
        self.isd = isd

    def debt_per_student(self):
        return self.hashify(self.context_debt_per_student())

    def debt_to_assessed_valuation(self):
        return self.hashify(self.context_debt_to_assessed_valuation())

    def debt_similar_school_size(self):
        return self.hashify(self.context_number_of_students())

    def similar_assessed_valuation(self):
        return self.hashify(self.context_assessed_valuation())

    def context_assessed_valuation(self):
        output = []
        tax_year_assessed_valuation = self.isd.tax_year_assessed_valuation

        if tax_year_assessed_valuation == None:
            return [self.isd]

        output = output + list(SchoolDistrictDebt.objects.filter(tax_year_assessed_valuation__gt=\
            tax_year_assessed_valuation).order_by('tax_year_assessed_valuation')[:2])

        output.append(self.isd)

        output = output + list(SchoolDistrictDebt.objects.filter(tax_year_assessed_valuation__lt=\
            tax_year_assessed_valuation).order_by('-tax_year_assessed_valuation')[:2])

        return output

    def context_number_of_students(self):
        output = []
        full_year_ada_2012 = self.isd.full_year_ada_2012

        if full_year_ada_2012 == None:
            return [self.isd]

        output = output + list(SchoolDistrictDebt.objects.filter(full_year_ada_2012__gt=\
            full_year_ada_2012).order_by('full_year_ada_2012')[:2])

        output.append(self.isd)
        output = output + list(SchoolDistrictDebt.objects.filter(full_year_ada_2012__lt=\
            full_year_ada_2012).order_by('-full_year_ada_2012')[:2])

        return output

    def context_debt_per_student(self):
        output = []
        total_debt_per_student = self.isd.total_debt_per_student

        if total_debt_per_student == None:
            return [self.isd]

        output = output + list(SchoolDistrictDebt.objects.filter(total_debt_per_student__gt=\
            total_debt_per_student).order_by('total_debt_per_student')[:2])

        output.append(self.isd)
        output = output + list(SchoolDistrictDebt.objects.filter(total_debt_per_student__lt=\
            total_debt_per_student).order_by('-total_debt_per_student')[:2])

        return output

    def context_debt_to_assessed_valuation(self):
        output = []
        total_debt_per_assessed_valuation = self.isd.total_debt_per_assessed_valuation

        if total_debt_per_assessed_valuation == None:
            return [self.isd]

        output = output + list(SchoolDistrictDebt.objects.filter(
            total_debt_per_assessed_valuation__gt=total_debt_per_assessed_valuation
            ).order_by('total_debt_per_assessed_valuation')[:2])

        output.append(self.isd)
        output = output + list(SchoolDistrictDebt.objects.filter(
            total_debt_per_assessed_valuation__lt=total_debt_per_assessed_valuation
            ).order_by('-total_debt_per_assessed_valuation')[:2])

        return output
