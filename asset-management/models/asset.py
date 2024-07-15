from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Asset(Base):
    __tablename__ = 'assets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    acquisition_date = Column(Date, nullable=False)
    maintenance_records = relationship('Maintenance', back_populates='asset')

    def __repr__(self):
        return f'<Asset(name={self.name}, acquisition_date={self.acquisition_date})>'
