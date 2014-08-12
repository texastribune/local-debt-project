from sqlalchemy import Column, String, Float, Date, Integer
from boot import Base


class CountyDebt(Base):
    __tablename__ = 'county_debt'

    id = Column(Integer, primary_key=True)
    created_at = Column(Date)
    govt_id = Column(String)
    issuer = Column(String)
    county = Column(String)
    debt_principal_outstanding = Column(Float)
    debt_interest_outstanding = Column(Float)
    debt_service_outstanding = Column(Float)
    m_and_o_tax_rate = Column(Float)
    i_and_s_tax_rate = Column(Float)
    total_tax_rate = Column(Float)
    tax_year_valuation = Column(Float)
    population = Column(Float)
    tax_debt_to_assessed_valuation = Column(Float)
    tax_debt_service_to_av = Column(Float)
    tax_debt_per_capita = Column(Float)

    data_file = '13cnytrlp.xls'
    data_position = range(7, 268)
    sheet = 'Tax-Supported Debt'
