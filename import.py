import os
import datetime
import xlrd

from boot import session
from lib import helpers
from models import *


def nullify_empty(cad):
    if cad == '':
        return None
    else:
        return cad


def import_city_and_county_debt():
    debt_models = [CityDebt, CountyDebt]

    for klass in debt_models:
        print "Importing %s" % klass.__name__
        xls = xlrd.open_workbook(os.path.join('data', klass.data_file))
        sheet = xls.sheet_by_name('Tax-Supported Debt')
        created_at = datetime.datetime.strptime('01052014', '%d%m%Y').date()
        debts = []
        for index in klass.data_position:
            row = sheet.row(index)
            debt = klass(
                created_at = created_at,
                govt_id = nullify_empty(row[0].value),
                issuer = nullify_empty(row[1].value),
                county = nullify_empty(row[2].value),
                debt_principal_outstanding = nullify_empty(row[3].value),
                debt_interest_outstanding = nullify_empty(row[4].value),
                debt_service_outstanding = nullify_empty(row[5].value),
                m_and_o_tax_rate = nullify_empty(row[6].value),
                i_and_s_tax_rate = nullify_empty(row[7].value),
                total_tax_rate = nullify_empty(row[8].value),
                tax_year_valuation = nullify_empty(row[9].value),
                population = nullify_empty(row[10].value),
                tax_debt_to_assessed_valuation = nullify_empty(row[11].value),
                tax_debt_service_to_av = nullify_empty(row[12].value),
                tax_debt_per_capita = nullify_empty(row[13].value)
                )
            debts.append(debt)
        helpers.store_objects(debts)


def import_school_district_debt():
    print "Importing 13VotedDebt for School Districts"
    xls = xlrd.open_workbook(os.path.join('data', SchoolDistrictDebt.data_file))
    voted_debt_sheet = xls.sheet_by_name('13VotedDebt')
    mo_debt_sheet = xls.sheet_by_name('13M&O Debt')
    created_at = datetime.datetime.strptime('01052014', '%d%m%Y').date()
    debts = []

    for index in SchoolDistrictDebt.sheets['13VotedDebt']:
        voted_row = voted_debt_sheet.row(index)
        debt = SchoolDistrictDebt(
            created_at = created_at,
            govt_id = voted_row[0].value,
            issuer = voted_row[1].value,
            county = voted_row[2].value,
            voter_approved_debt_service_outstanding = nullify_empty(voted_row[5].value),
            adopted_m_and_o_tax_rate_2011_voted = nullify_empty(voted_row[6].value),
            adopted_i_and_s_tax_rate_voted = nullify_empty(voted_row[7].value)
            )
        debts.append(debt)
    helpers.store_objects(debts)

    for index in SchoolDistrictDebt.sheets['13M&O Debt']:
        mo_row = mo_debt_sheet.row(index)
        school_debt = session.query(SchoolDistrictDebt).filter(SchoolDistrictDebt.govt_id == mo_row[0].value).first()

        if school_debt != None:
            school_debt.m_and_o_debt_service_outstanding = nullify_empty(mo_row[5].value)
            school_debt.adopted_m_and_o_tax_rate_2011 = nullify_empty(mo_row[6].value)
            school_debt.adopted_i_and_s_tax_rate = nullify_empty(mo_row[7].value)

            helpers.store_object(school_debt)


if __name__ == "__main__":
    print "Starting..."
    import_city_and_county_debt()
    import_school_district_debt()
