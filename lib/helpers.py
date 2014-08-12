from boot import session


def store_objects(objects):
    for obj in objects:
        store_object(obj)

def store_object(obj):
    try:
        session.add(obj)
        session.commit()
    except Exception as e:
        session.rollback()


class Export(object):
    def to_dict(self):
        return {
            'Govt ID': self.govt_id,
            'Issuer/Government Name': self.issuer,
            'County': self.county,
            'Debt Service': self.debt_service_outstanding,
            'M&O': self.m_and_o_tax_rate,
            'I&S': self.i_and_s_tax_rate,
            'Assesed Valuation': self.tax_year_valuation,
            'Population': self.population,
            'Tax Debt Service to AV': self.tax_debt_service_to_av,
            'Tax Debt Per Capita': self.tax_debt_per_capita
        }
