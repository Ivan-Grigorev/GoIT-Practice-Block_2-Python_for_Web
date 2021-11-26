from pymongo import MongoClient, DESCENDING, ASCENDING

client = MongoClient('mongodb+srv://MikeYatsenko:v320@cluster0.jja9n.mongodb.net/myFirstDatabase?retryWrites=true&w'
                     '=majority')

with client:
    db = client.testdb_2
    # for worker in workers:
    #     print(f'{worker["name"]} gets: {worker["salary"]}')
    #

    # print(workers.next())
    # print(workers.next())
    # print(workers.next())
    # print(workers.next())
    # workers.rewind()

    # query_1 = db.workers.find({'salary': {'$gte': 50000, '$lt': 80000}})
    #
    # [print(worker['name']) for worker in query_1]

    query_2 = db.workers.find().sort("salary", DESCENDING).limit(3)

    [print(worker['name'], worker['salary']) for worker in query_2]

    agr_query_3 = list(db.workers.aggregate([{'$group': {'_id': False,
                                                         'total': {
                                                             '$sum': "$salary"
                                                         },
                                                         'average_salary': {
                                                             '$avg': "$salary"
                                                         },
                                                         'min_salary': {
                                                             '$min': "$salary"
                                                         },
                                                         'max_salary': {
                                                             '$max': "$salary"
                                                         }
                                                         }
                                              }
                                             ]
                                            ))

    print(agr_query_3)
