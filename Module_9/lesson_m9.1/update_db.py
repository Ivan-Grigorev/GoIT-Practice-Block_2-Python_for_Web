from datetime import date
from sqlalchemy import func
from product import Product
from base import Session, engine, Base
from printer import Printer
from pc import PC
from laptop import Laptop

session = Session()

i = session.query(PC).get(3)
i.price = 1200
i.speed = 2800
session.add(i)
session.commit()

session.query(Printer).filter(
    Printer.printer_type.ilike("%atri%")
).update({"color": True}, synchronize_session='fetch')
session.commit()
