from debt_compare.models import SchoolDistrictDebt


class SchoolDistrictCompareService(object):
    def __init__(self, school_district_id):
        self.school_district_id = school_district_id
        self.school_district = SchoolDistrictDebt.objects.get(school_district_id)

