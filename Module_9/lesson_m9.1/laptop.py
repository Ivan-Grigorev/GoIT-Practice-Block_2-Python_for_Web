from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Laptop(Base):
    __tablename__ = 'laptop'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    speed = Column(Integer)
    ram = Column(Integer)
    hd = Column(Integer)
    screen = Column(Integer)
    price = Column(Integer)
    added_at = Column(Date)
    product = relationship("Product", backref='laptop')

    def __init__(self, product, speed, ram, hd, screen, price, added_at):
        self.product = product
        self.speed = speed
        self.ram = ram
        self.hd = hd
        self.screen = screen
        self.price = price
        self.added_at = added_at
