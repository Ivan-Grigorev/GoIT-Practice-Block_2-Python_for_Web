from base import Session, engine, Base
from printer import Printer
from pc import PC
from product import Product
from laptop import Laptop

session = Session()

i = session.query(PC).join(Product).filter(Product.maker == 'Apple').first()
session.delete(i)
session.commit()

session.query(Laptop).filter(
    Laptop.name.ilike("K%")
).delete(synchronize_session='fetch')
session.commit()