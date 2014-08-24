from debt_context.context_base import ContextBase
from debt_context.models import SchoolDistrictDebt


class ISDContextService(ContextBase):
    def __init__(self, isd):
        self.isd = isd

    def debt_per_student(self):
        return self.hashify(self.context_debt_per_student())

    def debt_to_assessed_valuation(self):
        return self.hashify(self.context_debt_to_assessed_valuation())

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
