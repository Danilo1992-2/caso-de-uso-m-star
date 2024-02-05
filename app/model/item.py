from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class EntryItem(Base):
    __tablename__: str = "entryItem"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    date: DateTime = Column(DateTime()) 
    product_id: int = Column(Integer, ForeignKey("product.id"))
    product = relationship("Product", back_populates="entryItem", uselist=False)

class OutputItem(Base):
    __tablename__: str = "outputItem"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    date: DateTime = Column(DateTime())
    product_id: int = Column(Integer, ForeignKey("product.id"))
    product = relationship("Product", back_populates="outputItem", uselist=False)

