from django.db import models


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


class SchoolDistrictDebt(models.Model):
    created_at = models.DateField()

    govt_id = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    county = models.CharField(max_length=200)

    # 13VotedDebt
    voter_approved_debt_service_outstanding = models.FloatField(null=True)
    adopted_m_and_o_tax_rate_2011_voted     = models.FloatField(null=True)
    adopted_i_and_s_tax_rate_voted          = models.FloatField(null=True)

    # 13M&O Debt
    m_and_o_debt_service_outstanding = models.FloatField(null=True)
    adopted_m_and_o_tax_rate_2011    = models.FloatField(null=True)
    adopted_i_and_s_tax_rate         = models.FloatField(null=True)

    sheets= {
        '13VotedDebt': range(7, 1027),
        '13M&O Debt':  range(7, 1028)
        }
    data_file = '13isdvamorvlp.xls'
