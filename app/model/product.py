from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class Product(Base):
    __tablename__: str = "product"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    product_name: str = Column(String(50))
    product_type: str = Column(String(20))
    product_code: str = Column(String(10), unique=True)
    product_manufacturer: str = Column(String(20))
    description: str = Column(String(200))
    createat: DateTime = Column(DateTime())
    user_id: int = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="product", uselist=False)
    entryItem = relationship("EntryItem", back_populates="product", uselist=False)
    outputItem = relationship("OutputItem", back_populates="product", uselist=False)