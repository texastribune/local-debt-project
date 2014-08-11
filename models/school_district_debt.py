from sqlalchemy import Column, String, Float, Date, Integer
from boot import Base


class SchoolDistrictDebt(Base):
    __tablename__ = 'school_district_debt'

    id = Column(Integer, primary_key=True)
    created_at = Column(Date)
    govt_id = Column(String)
    issuer = Column(String)
    county = Column(String)

    # 13VotedDebt
    voter_approved_debt_service_outstanding = Column(Float)
    adopted_m_and_o_tax_rate_2011_voted = Column(Float)
    adopted_i_and_s_tax_rate_voted = Column(Float)

    # 13M&O Debt
    m_and_o_debt_service_outstanding = Column(Float)
    adopted_m_and_o_tax_rate_2011 = Column(Float)
    adopted_i_and_s_tax_rate = Column(Float)

    sheets= {
        '13VotedDebt': range(7, 1027),
        '13M&O Debt':  range(7, 1028)
        }
    data_file = '13isdvamorvlp.xls'
