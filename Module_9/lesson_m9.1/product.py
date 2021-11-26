from sqlalchemy import Column, String, Integer, Date

from base import Base


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    maker = Column(String)
    product_type = Column(String)

    def __init__(self, maker, product_type):
        self.maker = maker
        self.product_type = product_type
