from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from bson.objectid import ObjectId
import sys
import os

# Add Backend folder to path to import db
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import customers_collection, restaurants_collection, foods_collection, cart_collection, orders_collection

def get_data(request):
    if request.body:
        return json.loads(request.body)
    return {}

def serialize_doc(doc):
    if doc and '_id' in doc:
        doc['id'] = str(doc['_id'])
        del doc['_id']
    return doc

# --- Customer APIs ---
@csrf_exempt
def customer_add(request):
    if request.method == 'POST':
        data = get_data(request)
        result = customers_collection.insert_one(data)
        return JsonResponse({"message": "Customer added", "id": str(result.inserted_id)})

def customer_list(request):
    if request.method == 'GET':
        customers = [serialize_doc(doc) for doc in customers_collection.find()]
        return JsonResponse(customers, safe=False)

@csrf_exempt
def customer_update(request, id):
    if request.method == 'PUT':
        data = get_data(request)
        customers_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return JsonResponse({"message": "Customer updated"})

@csrf_exempt
def customer_delete(request, id):
    if request.method == 'DELETE':
        customers_collection.delete_one({"_id": ObjectId(id)})
        return JsonResponse({"message": "Customer deleted"})

# --- Restaurant APIs ---
@csrf_exempt
def restaurant_add(request):
    if request.method == 'POST':
        data = get_data(request)
        result = restaurants_collection.insert_one(data)
        return JsonResponse({"message": "Restaurant added", "id": str(result.inserted_id)})

def restaurant_list(request):
    if request.method == 'GET':
        restaurants = [serialize_doc(doc) for doc in restaurants_collection.find()]
        return JsonResponse(restaurants, safe=False)

@csrf_exempt
def restaurant_update(request, id):
    if request.method == 'PUT':
        data = get_data(request)
        restaurants_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return JsonResponse({"message": "Restaurant updated"})

@csrf_exempt
def restaurant_delete(request, id):
    if request.method == 'DELETE':
        restaurants_collection.delete_one({"_id": ObjectId(id)})
        return JsonResponse({"message": "Restaurant deleted"})

# --- FoodItem APIs ---
@csrf_exempt
def food_add(request):
    if request.method == 'POST':
        data = get_data(request)
        result = foods_collection.insert_one(data)
        return JsonResponse({"message": "Food item added", "id": str(result.inserted_id)})

def food_list(request):
    if request.method == 'GET':
        foods = [serialize_doc(doc) for doc in foods_collection.find()]
        return JsonResponse(foods, safe=False)

@csrf_exempt
def food_update(request, id):
    if request.method == 'PUT':
        data = get_data(request)
        foods_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return JsonResponse({"message": "Food item updated"})

@csrf_exempt
def food_delete(request, id):
    if request.method == 'DELETE':
        foods_collection.delete_one({"_id": ObjectId(id)})
        return JsonResponse({"message": "Food item deleted"})

# --- Cart APIs ---
@csrf_exempt
def cart_add(request):
    if request.method == 'POST':
        data = get_data(request)
        result = cart_collection.insert_one(data)
        return JsonResponse({"message": "Cart item added", "id": str(result.inserted_id)})

def cart_list(request):
    if request.method == 'GET':
        carts = [serialize_doc(doc) for doc in cart_collection.find()]
        return JsonResponse(carts, safe=False)

@csrf_exempt
def cart_update(request, id):
    if request.method == 'PUT':
        data = get_data(request)
        cart_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return JsonResponse({"message": "Cart item updated"})

@csrf_exempt
def cart_delete(request, id):
    if request.method == 'DELETE':
        cart_collection.delete_one({"_id": ObjectId(id)})
        return JsonResponse({"message": "Cart item deleted"})

# --- Order APIs ---
@csrf_exempt
def order_add(request):
    if request.method == 'POST':
        data = get_data(request)
        result = orders_collection.insert_one(data)
        return JsonResponse({"message": "Order added", "id": str(result.inserted_id)})

def order_list(request):
    if request.method == 'GET':
        orders = [serialize_doc(doc) for doc in orders_collection.find()]
        return JsonResponse(orders, safe=False)

@csrf_exempt
def order_update(request, id):
    if request.method == 'PUT':
        data = get_data(request)
        orders_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return JsonResponse({"message": "Order updated"})

@csrf_exempt
def order_delete(request, id):
    if request.method == 'DELETE':
        orders_collection.delete_one({"_id": ObjectId(id)})
        return JsonResponse({"message": "Order deleted"})
