from pymongo import MongoClient


def get_db(collection = 'abc', db_name= 'dump2data'):
    try:
        conn = MongoClient()
        db = conn[db_name]
        print("Connected successfully!!!")
        collection_x1 = db[collection]
        # return db.HINDUNILVR_op1
        return collection_x1
    except Exception as e:
        print("Could not connect to MongoDB" , e)
mydict = { "name": "John", "address": "Highway 37" }
get_db("abcd", "axc").insert_one({"mydict": "d"})