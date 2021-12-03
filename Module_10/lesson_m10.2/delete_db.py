from pymongo import MongoClient


client = MongoClient('mongodb+srv://MikeYatsenko:v320@cluster0.jja9n.mongodb.net/myFirstDatabase?retryWrites=true&w'
                     '=majority')
with client:
    db = client.testdb_2

    workers = db.workers

    # workers.delete_one({'name':'John May'})

    query = {"salary": {"$lt": 50000}}
    d = workers.delete_many(query)

    print(d.deleted_count, "documents deleted!")
