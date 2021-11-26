from datetime import date

from product import Product
from base import Session, engine, Base
from printer import Printer
from pc import PC
from laptop import Laptop

# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

# 4 - create product seed data
samsung_pc = Product("Samsung", 'PC')
apple_pc = Product("Apple", 'PC')
hp_pc = Product("Hewlett-Packard", 'PC')

lenovo_laptop = Product("Lenovo", 'Laptop')
apple_laptop = Product("Apple", 'Laptop')
hp_laptop = Product('Hewlett-Packard', "Laptop")

canon_printer = Product("Canon", 'Printer')
konica_printer = Product("Konica Minolta", "Printer")
samsung_printer = Product("Samsung", "Printer")

# 5 - create pc seed data
pc_1 = PC(samsung_pc, 2200, 16, 250, 800, date.today().isoformat())
pc_2 = PC(apple_pc, 3500, 32, 1000, 1600, date.today().isoformat())
pc_3 = PC(samsung_pc, 3000, 32, 500, 1200, date(2021, 11, 5))
pc_4 = PC(hp_pc, 2500, 16, 500, 1000, date.today().isoformat())
pc_5 = PC(apple_pc, 4400, 1500, 8000, 50000, date.today().isoformat())
pc_6 = PC(hp_pc, 1800, 8, 150, 650, date(2021, 11, 3))

# 6 - create laptop seed data
lp_1 = Laptop(lenovo_laptop, 2000, 16, 250, 850, 15, date.today().isoformat())
lp_2 = Laptop(apple_laptop, 2800, 32, 1000, 1400, 13, date.today().isoformat())
lp_3 = Laptop(hp_laptop, 2800, 32, 250, 1200, 15, date(2021, 11, 5))
lp_4 = Laptop(hp_laptop, 3000, 16, 500, 1000, 17, date.today().isoformat())
lp_5 = Laptop(apple_laptop, 2500, 64, 1000, 2550, 13, date.today().isoformat())
lp_6 = Laptop(lenovo_laptop, 2000, 8, 250, 950, 17, date(2021, 11, 3))

# 7 - create printer seed data
pr_1 = Printer(canon_printer, True, 'Laser', 400, date.today().isoformat())
pr_2 = Printer(canon_printer, False, 'Matrix', 100, date.today().isoformat())
pr_3 = Printer(konica_printer, True, 'Laser', 650, date.today().isoformat())
pr_4 = Printer(samsung_printer, False, 'Jet', 90, date.today().isoformat())
pr_5 = Printer(samsung_printer, True, 'Matrix', 150,date(2021, 11, 5))
pr_6 = Printer(canon_printer, True, 'Jet', 250, date(2021, 11, 3))


session.add(samsung_pc)
session.add(apple_pc)
session.add(hp_pc)
session.add(lenovo_laptop)
session.add(apple_laptop)
session.add(hp_laptop)
session.add(canon_printer)
session.add(konica_printer)
session.add(samsung_printer)


session.add(pc_1)
session.add(pc_2)
session.add(pc_3)
session.add(pc_4)
session.add(pc_5)
session.add(pc_6)


session.add(lp_1)
session.add(lp_2)
session.add(lp_3)
session.add(lp_4)
session.add(lp_5)
session.add(lp_6)

session.add(pr_1)
session.add(pr_2)
session.add(pr_3)
session.add(pr_4)
session.add(pr_5)
session.add(pr_6)


session.commit()
session.close()

