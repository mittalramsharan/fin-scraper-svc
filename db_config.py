from pymongo import MongoClient


def get_db(collection = 'abc'):
    try:
        conn = MongoClient()
        db = conn.dump2data
        print("Connected successfully!!!")
        collection_x1 = db[collection]
        # return db.HINDUNILVR_op1
        return collection_x1
    except Exception as e:
        print("Could not connect to MongoDB" , e)
mydict = { "name": "John", "address": "Highway 37" }
get_db("abcd").insert_one({"mydict": "d"})