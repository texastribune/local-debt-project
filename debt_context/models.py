from django.db import models
from boundaries.models import Shape


def n_a_if_none(value):
    if value == None:
        return 'N/A'
    else:
        return value


class CityDebt(models.Model):
    created_at = models.DateField()

    govt_id = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    county = models.CharField(max_length=200)

    debt_principal_outstanding     = models.FloatField(null=True)
    debt_interest_outstanding      = models.FloatField(null=True)
    debt_service_outstanding       = models.FloatField(null=True)
    m_and_o_tax_rate               = models.FloatField(null=True)
    i_and_s_tax_rate               = models.FloatField(null=True)
    total_tax_rate                 = models.FloatField(null=True)
    tax_year_valuation             = models.FloatField(null=True)
    population                     = models.IntegerField(null=True)
    tax_debt_to_assessed_valuation = models.FloatField(null=True)
    tax_debt_service_to_av         = models.FloatField(null=True)
    tax_debt_per_capita            = models.FloatField(null=True)
    shape                          = models.ForeignKey(Shape)

    data_file = '14citytrlp.xls'
    data_position = range(7, 1240)
    sheet_name = 'Tax-Supported Debt'
    issuer_type = 'city'

    def to_dict(self):
        return {
            'issuer': self.issuer,
            'county': self.county,
            'debtPrincipal': n_a_if_none(self.debt_principal_outstanding),
            'debtInterest': n_a_if_none(self.debt_interest_outstanding),
            'debtService': n_a_if_none(self.debt_service_outstanding),
            'population': n_a_if_none(self.population),
            'taxDebtPerCapita': n_a_if_none(self.tax_debt_per_capita),
            'taxDebtToAssessedValuation': n_a_if_none(self.tax_debt_to_assessed_valuation),
            'issuerType': 'city'
        }

    def to_short_dict(self):
        return {
            'issuer': self.issuer,
            'debtPrincipal': n_a_if_none(self.debt_principal_outstanding),
            'population': n_a_if_none(self.population),
            'taxDebtPerCapita': n_a_if_none(self.tax_debt_per_capita),
            'taxDebtToAssessedValuation': n_a_if_none(self.tax_debt_to_assessed_valuation),
            'taxYearValuation': n_a_if_none(self.tax_year_valuation),
            'issuerType': 'city'
        }

    def __cmp__(self, other):
        if other.issuer_type == 'county':
            return 1
        elif other.issuer_type == 'isd':
            return -1
        else:
            return 0


class CountyDebt(models.Model):
    created_at = models.DateField()

    govt_id = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    county = models.CharField(max_length=200)

    debt_principal_outstanding     = models.FloatField(null=True)
    debt_interest_outstanding      = models.FloatField(null=True)
    debt_service_outstanding       = models.FloatField(null=True)
    m_and_o_tax_rate               = models.FloatField(null=True)
    i_and_s_tax_rate               = models.FloatField(null=True)
    total_tax_rate                 = models.FloatField(null=True)
    tax_year_valuation             = models.FloatField(null=True)
    population                     = models.IntegerField(null=True)
    tax_debt_to_assessed_valuation = models.FloatField(null=True)
    tax_debt_service_to_av         = models.FloatField(null=True)
    tax_debt_per_capita            = models.FloatField(null=True)
    shape                          = models.ForeignKey(Shape)

    data_file = '14cnytrlp.xls'
    data_position = range(7, 268)
    sheet_name = 'Tax-Supported Debt'
    issuer_type = 'county'

    def to_dict(self):
        return {
            'issuer': self.issuer,
            'debtPrincipal': n_a_if_none(self.debt_principal_outstanding),
            'debtInterest': n_a_if_none(self.debt_interest_outstanding),
            'debtService': n_a_if_none(self.debt_service_outstanding),
            'population': n_a_if_none(self.population),
            'taxDebtPerCapita': n_a_if_none(self.tax_debt_per_capita),
            'taxDebtToAssessedValuation': n_a_if_none(self.tax_debt_to_assessed_valuation),
            'issuerType': 'county'
        }

    def to_short_dict(self):
        return {
            'issuer': self.issuer,
            'debtPrincipal': n_a_if_none(self.debt_principal_outstanding),
            'population': n_a_if_none(self.population),
            'taxDebtPerCapita': n_a_if_none(self.tax_debt_per_capita),
            'taxDebtToAssessedValuation': n_a_if_none(self.tax_debt_to_assessed_valuation),
            'taxYearValuation': n_a_if_none(self.tax_year_valuation),
            'issuerType': 'county'
        }

    def __cmp__(self, other):
        if other.issuer_type == 'city':
            return -1
        elif other.issuer_type == 'isd':
            return -2
        else:
            return 0


class SchoolDistrictDebt(models.Model):
    created_at = models.DateField()

    govt_id = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    county = models.CharField(max_length=200)
    shape = models.ForeignKey(Shape)

    # General info
    tax_year_assessed_valuation               = models.FloatField(null=True)
    full_year_ada_2012                        = models.IntegerField(null=True)

    # 13VotedDebt
    voter_approved_debt_principal_outstanding = models.FloatField(null=True)
    voter_approved_debt_interest_outstanding  = models.FloatField(null=True)
    voter_approved_debt_service_outstanding   = models.FloatField(null=True)

    # 13M&O Debt
    m_and_o_debt_principal_outstanding = models.FloatField(null=True)
    m_and_o_debt_interest_outstanding  = models.FloatField(null=True)
    m_and_o_debt_service_outstanding   = models.FloatField(null=True)

    # Composed fields
    total_debt_per_student            = models.FloatField(null=True)
    total_debt_per_assessed_valuation = models.FloatField(null=True)
    combined_principal_debt           = models.FloatField(null=True)

    sheets= {
        '14VotedDebt': range(7, 1027),
        '14M&O Debt':  range(7, 1028)
        }
    data_file = '14isdvamorvlp.xls'
    issuer_type = 'isd'

    def to_dict(self):
        return  {
            'issuer': self.issuer,
            'students':                   n_a_if_none(self.full_year_ada_2012),
            'taxYearAssessedValuation':   n_a_if_none(self.tax_year_assessed_valuation),
            'debtPerStudent':             n_a_if_none(self.total_debt_per_student),
            'totalDebtPerAV':             n_a_if_none(self.total_debt_per_assessed_valuation),
            'voterApprovedDebtPrincipal': n_a_if_none(self.voter_approved_debt_principal_outstanding),
            'voterApprovedDebtInterest':  n_a_if_none(self.voter_approved_debt_interest_outstanding),
            'voterApprovedDebtService':   n_a_if_none(self.voter_approved_debt_service_outstanding),
            'mODebtPrincipal':            n_a_if_none(self.m_and_o_debt_principal_outstanding),
            'mODebtInterest':             n_a_if_none(self.m_and_o_debt_interest_outstanding),
            'mODebtService':              n_a_if_none(self.m_and_o_debt_service_outstanding),
            'combinedDebt':               n_a_if_none(self.combined_principal_debt),
            'issuerType':                 'isd'
        }

    def to_short_dict(self):
        return {
            'issuer': self.issuer,
            'combinedDebt': self.combined_principal_debt,
            'totalDebtPerStudent': self.total_debt_per_student,
            'taxYearAssessedValuation': self.tax_year_assessed_valuation,
            'totalDebtPerAV': self.total_debt_per_assessed_valuation,
            'students': self.full_year_ada_2012
        }

    def __cmp__(self, other):
        if other.issuer_type == 'county':
            return 2
        elif other.issuer_type == 'isd':
            return 1
        else:
            return 0
