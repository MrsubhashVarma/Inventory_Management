from pymongo import MongoClient
import os

# Connection string provided by the user
MONGO_URI = "mongodb+srv://SubhasVarma:Sjv$007@cluster0.0fbfiti.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client['food_delivery']

# Collections
customers_collection = db['customers']
restaurants_collection = db['restaurants']
foods_collection = db['foods']
cart_collection = db['cart']
orders_collection = db['orders']
