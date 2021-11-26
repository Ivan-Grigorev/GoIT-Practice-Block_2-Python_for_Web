from datetime import date
from sqlalchemy import func
from product import Product
from base import Session, engine, Base
from printer import Printer
from pc import PC
from laptop import Laptop

session = Session()

computers = session.query(PC).all()

print('All PCs:', '\n')

for computer in computers:
    print(f'PC price:{computer.price} and it was released on {computer.added_at}')

printer_makers = session.query(Product.maker).filter(Product.product_type == 'Printer').all()
print('All printer makers:' '\n')
print(printer_makers)

pc_specific_date = session.query(PC).filter(PC.added_at > date(2021, 11, 5))
print(pc_specific_date)

pc_data = session.query(PC).join(Product).filter(Product.maker == 'Apple').all()

for computer in pc_data:
    print(f'PC speed is {computer.speed}')


max_pc_price = session.query(func.max(PC.speed)).all()
print(max_pc_price)