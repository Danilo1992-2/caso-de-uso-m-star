from sqlalchemy import (Column, Integer, Float, String, Date, ForeignKey)
from sqlalchemy.orm import relationship
from config import Base



class User(Base):
    __tablename__: str = "user"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(50))
    document: str = Column(String(11))
    password: str = Column(String(50))
    product = relationship('Product', back_populates='user', uselist=False)
