from django.db import models


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
    population                     = models.FloatField(null=True)
    tax_debt_to_assessed_valuation = models.FloatField(null=True)
    tax_debt_service_to_av         = models.FloatField(null=True)
    tax_debt_per_capita            = models.FloatField(null=True)

    data_file = '13citytrlp.xls'
    data_position = range(7, 1240)
    sheet_name = 'Tax-Supported Debt'

    def to_dict(self):
        return {
            'id': self.id,
            'Govt ID': self.govt_id,
            'Issuer': self.issuer,
            'County': self.county,
            'Debt Principal': n_a_if_none(self.debt_principal_outstanding),
            'Debt Interest': n_a_if_none(self.debt_interest_outstanding),
            'Debt Service': n_a_if_none(self.debt_service_outstanding),
            'Population': n_a_if_none(self.population),
            'Tax Debt Per Capita': n_a_if_none(self.tax_debt_per_capita)
        }


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
    population                     = models.FloatField(null=True)
    tax_debt_to_assessed_valuation = models.FloatField(null=True)
    tax_debt_service_to_av         = models.FloatField(null=True)
    tax_debt_per_capita            = models.FloatField(null=True)

    data_file = '13cnytrlp.xls'
    data_position = range(7, 268)
    sheet_name = 'Tax-Supported Debt'

    def to_dict(self):
        return {
            'id': self.id,
            'Govt ID': self.govt_id,
            'Issuer': self.issuer,
            'County': self.county,
            'Debt Principal': n_a_if_none(self.debt_principal_outstanding),
            'Debt Interest': n_a_if_none(self.debt_interest_outstanding),
            'Debt Service': n_a_if_none(self.debt_service_outstanding),
            'Population': n_a_if_none(self.population),
            'Tax Debt Per Capita': n_a_if_none(self.tax_debt_per_capita)
        }


class SchoolDistrictDebt(models.Model):
    created_at = models.DateField()

    govt_id = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    county = models.CharField(max_length=200)

    # 13VotedDebt
    voter_approved_debt_principal_outstanding = models.FloatField(null=True)
    voter_approved_debt_interest_outstanding  = models.FloatField(null=True)
    voter_approved_debt_service_outstanding   = models.FloatField(null=True)
    voter_approved_full_year_ada_2012         = models.FloatField(null=True)

    # 13M&O Debt
    m_and_o_debt_principal_outstanding = models.FloatField(null=True)
    m_and_o_debt_interest_outstanding  = models.FloatField(null=True)
    m_and_o_debt_service_outstanding   = models.FloatField(null=True)
    m_and_o_full_year_ada_2012         = models.FloatField(null=True)

    sheets= {
        '13VotedDebt': range(7, 1027),
        '13M&O Debt':  range(7, 1028)
        }
    data_file = '13isdvamorvlp.xls'

    def to_dict(self):
        return  {
            'id': self.id,
            'Govt ID': self.govt_id,
            'Issuer': self.issuer,
            'County': self.county,
            'Voter-Approved Debt Principal': n_a_if_none(self.voter_approved_debt_principal_outstanding),
            'Voter-Approved Debt Interest':  n_a_if_none(self.voter_approved_debt_interest_outstanding),
            'Voter-Approved Debt Service':   n_a_if_none(self.voter_approved_debt_service_outstanding),
            'Voter-Approved ADA2012':        n_a_if_none(self.voter_approved_full_year_ada_2012),
            'M&O Debt Principal':            n_a_if_none(self.m_and_o_debt_principal_outstanding),
            'M&O Debt Interest':             n_a_if_none(self.m_and_o_debt_interest_outstanding),
            'M&O Debt Service':              n_a_if_none(self.m_and_o_debt_service_outstanding),
            'M&O ADA2012':                   n_a_if_none(self.m_and_o_full_year_ada_2012)
        }
