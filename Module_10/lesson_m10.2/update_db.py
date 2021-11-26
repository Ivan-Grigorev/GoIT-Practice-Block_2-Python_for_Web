from pymongo import MongoClient

client = MongoClient('mongodb+srv://MikeYatsenko:v320@cluster0.jja9n.mongodb.net/myFirstDatabase?retryWrites=true&w'
                     '=majority')
with client:
    db = client.testdb_2

    workers = db.workers

    filter_value = {'name': 'Cristian Benjamin'}
    new_value = {"$set": {'salary': 56000}}

    workers.update_one(filter_value, new_value)

    # Printing the updated content of the
    # database
    worker_cris = workers.find_one({"name": 'Cristian Benjamin'})
    print(worker_cris['salary'])

    filter_value = {'name': {'$regex': 's'}}

    new_value = {'$set': {'company': 'S_company'}}

    workers.update_many(filter_value, new_value)
    
    for worker in workers.find():
        print(worker['company'])
