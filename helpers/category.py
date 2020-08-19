from Catalogger import app
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import firestore
from helpers.auth import *
import pyrebase

config = {
        "apiKey": "AIzaSyCvfS9pbQotKpJVtG3nrtIRgChnh99lX4U",
        "authDomain": "catalogger-68d96.firebaseapp.com",
        "databaseURL": "https://catalogger-68d96.firebaseio.com",
        "storageBucket": "catalogger-68d96.appspot.com",
    }
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
#cred = credentials.Certificate(app.config['FIRESTORE_KEY_PATH'])
#firebase_admin.initialize_app(cred)

firestore_client = firestore.client()
    
def getProductsInfo(business_id,category_id,sub_category_id):
    product_list = []
    for k in firestore_client.collection('businesses').document(business_id).collection('categories').document(category_id).collection('subcategories').document(sub_category_id).collection('products').get():
        product_category_id = k.id
        product_category_name = k.to_dict()['name']
        product_category_description = k.to_dict()['description']
        product_category_price = k.to_dict()['price']
        product_list.append({'name':product_category_name,'id':product_category_id,'description':product_category_description,'price':product_category_price})    
    return product_list

def addProducts(category_id,sub_category_id,product_name,product_desc,product_price,business_id,img):
    _,product = firestore_client.collection('businesses').document(business_id).collection('categories').document(category_id).collection('subcategories').document(sub_category_id).collection('products').add({
        'name':product_name,
        'description':product_desc,
        'price':product_price
    }) 
    _,link = storage.child(business_id+'/'+category_id+'/'+sub_category_id+'/'+product.id).put(img)
    print(link)
    return True

def addCategory(name,business_id):
    firestore_client.collection('businesses').document(business_id).collection('categories').add({
        'name':name
    })
    return True

def addSubCategory(category_id,name,business_id):
    firestore_client.collection('businesses').document(business_id).collection('categories').document(category_id).collection('subcategories').add({
        'name':name
    })
    return True

