from sqlalchemy import Column, String, Integer, Date, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from base import Base


class Printer(Base):
    __tablename__ = 'printer'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    color = Column(Boolean)  # True if color
    printer_type = Column(Text)
    price = Column(Integer)
    added_at = Column(Date)
    product = relationship("Product", backref='printer')

    def __init__(self, product, color, printer_type, price,added_at):
        self.product = product
        self.color = color
        self.printer_type = printer_type
        self.price = price
        self.added_at = added_at
