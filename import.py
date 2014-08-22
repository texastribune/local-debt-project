import os
import datetime
import xlrd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "local_debt.settings")
from debt_context.models import CityDebt, CountyDebt, SchoolDistrictDebt


def nullify_empty(cad):
    if cad == '':
        return None
    else:
        return cad

def total_debt(school_debt):
    va_debt = school_debt.voter_approved_debt_principal_outstanding
    mo_debt = school_debt.m_and_o_debt_principal_outstanding

    return (0 if va_debt == None else va_debt) + (0 if mo_debt == None else mo_debt)

def debt_per_student(school_debt):
    ada = school_debt.full_year_ada_2012

    if ada == None or ada == 0:
        return None
    else:
        return total_debt(school_debt) / ada

def debt_per_assessed_valuation(school_debt):
    av = school_debt.tax_year_assessed_valuation

    if av == None or av == 0:
        return None
    else:
        return total_debt(school_debt) / av

def import_city_and_county_debt():
    debt_models = [CityDebt, CountyDebt]

    for klass in debt_models:
        print "Importing %s" % klass.__name__
        xls = xlrd.open_workbook(os.path.join('data', klass.data_file))
        sheet = xls.sheet_by_name(klass.sheet_name)
        created_at = datetime.datetime.strptime('01052014', '%d%m%Y').date()
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
            debt.save()


def import_school_district_debt():
    print "Importing 13VotedDebt for School Districts"
    xls = xlrd.open_workbook(os.path.join('data', SchoolDistrictDebt.data_file))
    voted_debt_sheet = xls.sheet_by_name('13VotedDebt')
    mo_debt_sheet = xls.sheet_by_name('13M&O Debt')
    created_at = datetime.datetime.strptime('01052014', '%d%m%Y').date()

    for index in SchoolDistrictDebt.sheets['13VotedDebt']:
        voted_row = voted_debt_sheet.row(index)
        debt = SchoolDistrictDebt(
            created_at = created_at,
            govt_id = voted_row[0].value,
            issuer = voted_row[1].value,
            county = voted_row[2].value,
            voter_approved_debt_principal_outstanding = nullify_empty(voted_row[3].value),
            voter_approved_debt_interest_outstanding  = nullify_empty(voted_row[4].value),
            voter_approved_debt_service_outstanding   = nullify_empty(voted_row[5].value),
            tax_year_assessed_valuation               = nullify_empty(voted_row[9].value),
            full_year_ada_2012                        = nullify_empty(voted_row[13].value)
            )
        debt.save()

    for index in SchoolDistrictDebt.sheets['13M&O Debt']:
        mo_row = mo_debt_sheet.row(index)
        try:
            school_debt = SchoolDistrictDebt.objects.get(govt_id=mo_row[0].value)
            school_debt.m_and_o_debt_principal_outstanding = nullify_empty(mo_row[3].value)
            school_debt.m_and_o_debt_interest_outstanding  = nullify_empty(mo_row[4].value)
            school_debt.m_and_o_debt_service_outstanding   = nullify_empty(mo_row[5].value)
            school_debt.save()
        except SchoolDistrictDebt.DoesNotExist:
            next

    for school_debt in SchoolDistrictDebt.objects.all():
        school_debt.total_debt_per_student = debt_per_student(school_debt)
        school_debt.total_debt_per_assessed_valuation = debt_per_assessed_valuation(school_debt)
        school_debt.save()


if __name__ == "__main__":
    print "Starting..."
    import_city_and_county_debt()
    import_school_district_debt()
