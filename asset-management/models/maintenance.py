from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Maintenance(Base):
    __tablename__ = 'maintenances'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    description = Column(String, nullable=False)
    asset_id = Column(Integer, ForeignKey('assets.id'), nullable=False)
    asset = relationship('Asset', back_populates='maintenance_records')

    def __repr__(self):
        return f'<Maintenance(date={self.date}, description={self.description})>'
