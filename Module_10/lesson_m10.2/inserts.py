from pymongo import MongoClient
from faker import Faker
import random
client = MongoClient(
    'mongodb+srv://MikeYatsenko:v320@cluster0.jja9n.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
fake = Faker()


workers = [
    {'name': fake.name(), 'company': fake.company(), 'enroll': fake.date(), 'salary': random.randint(20000, 120000)},
    {'name': fake.name(), 'company': fake.company(), 'enroll': fake.date(), 'salary': random.randint(20000, 120000)},
    {'name': fake.name(), 'company': fake.company(), 'enroll': fake.date(), 'salary': random.randint(20000, 120000)},
    {'name': fake.name(), 'company': fake.company(), 'enroll': fake.date(), 'salary': random.randint(20000, 120000)},
    {'name': fake.name(), 'company': fake.company(), 'enroll': fake.date(), 'salary': random.randint(20000, 120000)},
    {'name': fake.name(), 'company': fake.company(), 'enroll': fake.date(), 'salary': random.randint(20000, 120000)},
    {'name': fake.name(), 'company': fake.company(), 'enroll': fake.date(), 'salary': random.randint(20000, 120000)},
    {'name': fake.name(), 'company': fake.company(), 'enroll': fake.date(), 'salary': random.randint(20000, 120000)},
    {'name': fake.name(), 'company': fake.company(), 'enroll': fake.date(), 'salary': random.randint(20000, 120000)},
    {'name': fake.name(), 'company': fake.company(), 'enroll': fake.date(), 'salary': random.randint(20000, 120000)},


]

with client:
    db = client.testdb_2

    db.workers.insert_many(workers)
