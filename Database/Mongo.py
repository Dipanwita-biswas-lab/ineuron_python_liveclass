import pymongo

# pip install pymongo
# pip install "pymongo[srv]"
client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.a1alg.mongodb.net/?retryWrites=true&w=majority")
db = client.test

# database--> collection-- document

# create database
# -----------------------------------
database = client['ineuron']

# create table(collection)
# -----------------------------------
collection = database['genre']

# document
# # -----------------------------------
# data = {'movie_id': '12340'
#     , 'genre': ['Horror', 'Romantic']}
#
# # insert data 1 document
# # -----------------------------------
# collection.insert_one(data)

# insert data multiple documents
# -----------------------------------
data = [{'movie_id': 12340
    , 'genre': 'ROMANTIC'}
        , {'movie_id': 12341
    , 'genre': 'COMEDY'}
        ,{'movie_id': 12342
    , 'genre': 'POLITITCAL'}
        , {'movie_id': 12343
    , 'genre': 'TRUE STORY'}
        , {'movie_id': 12344
    , 'genre': 'DRAMA'}]

# insert data  multiple document
# -----------------------------------
collection.insert_many(data)

# # select *
# -----------------------------------
# for i in collection.find():
#     print(i)


# select where condition (=)
# -----------------------------------
data = collection.find({'movie_id': 12340})

# select where condition  (>)
# -----------------------------------
data = collection.find({'movie_id': {'$gt': 12340}})

data = collection.find({'$or':[{'genre': 'Comedy'},{'movie_id': {'$gte': 12340}}]})

# update statement
# -----------------------------------
# collection.update_one({'$and':[{'genre': 'Comedy'},{'movie_id': {'$gte': 12340}}]}, {'$set': {'genre':'Drama'}})

# delete statement
# -----------------------------------
# collection.delete_one({'$and':[{'genre': 'Comedy'},{'movie_id': {'$gte': 12340}}]}, {'$set': {'genre':'Drama'}})

for i in data:
    print(i)

# .where({'movie_id': {'$eq': '12340'}})
