from Catalogger import app
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import firestore
import pyrebase

config = {
        "apiKey": "AIzaSyCvfS9pbQotKpJVtG3nrtIRgChnh99lX4U",
        "authDomain": "catalogger-68d96.firebaseapp.com",
        "databaseURL": "https://catalogger-68d96.firebaseio.com",
        "storageBucket": "catalogger-68d96.appspot.com",
    }

cred = credentials.Certificate(app.config['FIRESTORE_KEY_PATH'])

firebase_admin.initialize_app(cred)
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

 
firestore_client = firestore.client()

def createUserAccount(name, email_id, password):
    try:
        user = auth.create_user(
            display_name=name,
            email=email_id,
            email_verified=True,
            password=password
        )
        firestore_client.collection('users').document(user.uid).set({
            'name': name,
            'ownerOf': "",
        })
        print("Created user", user.uid)
        return user.uid
    except:
        print("Error")
        return None

def createBusinessUserAccount(name,email_id, password,bname,bdesc,category,img):
        user = auth.create_user(
            display_name = bname,
            email = email_id,
            email_verified = True,
            password = password,
        )
        _,b_user = firestore_client.collection('businesses').add({
            'name': bname,
            'category':category,
            'description': bdesc,
            'ownedBy': user.uid
        })
        firestore_client.collection('users').document(user.uid).set({
            'name': name,
            'ownerOf': b_user.id
        })
        storage.child(b_user.id+'hh.jpg').put(img[0])
        firestore_client.collection('businesses').document(b_user.id).update({
        'image': storage.child(b_user.id+'hh.jpg').get_url(None)
    })
        print(name,email_id, password,bname,bdesc,category)
        return user.uid

def loginUserAccount(email_id, password):
    user = firebase.auth().sign_in_with_email_and_password(email_id, password)
    return user['localId']
    
def getBusinessInfo(userId):
    business = {}
    for i in firestore_client.collection('businesses').where('ownedBy','==',userId).get():
        business_id = i.id
        business_name = i.to_dict()['name']   
        return {'business_name':business_name,'business_id':business_id}

def getBusinessCategories(business_id):
    category_dict = {}
    categories = []
   
    for j in firestore_client.collection('businesses').document(business_id).collection('categories').get():
        business_category_name = j.to_dict()['name']
        categories.append({'name':business_category_name,'id':j.id,'subcategories':[]})

    for i in categories:
        for k in firestore_client.collection('businesses').document(business_id).collection('categories').document(i['id']).collection('subcategories').get():
            business_sub_category_id = k.id
            business_sub_category_name = k.to_dict()['name']
            i['subcategories'].append({'name':business_sub_category_name,'id':business_sub_category_id})
    return categories 

def searchProduct(search_key):
    businesses = []
    mylist = []
    for i in firestore_client.collection('businesses').get():
        business_id = i.id
        business_name = i.to_dict()['name']
        business_desc = i.to_dict()['description']
        business_image = i.to_dict()['image']
        businesses.append({'business_id':business_id,'business_name':business_name,'business_description':business_desc,'business_image':business_image})    
    for j in businesses:
        if search_key in j['business_name']:
            mylist.append(j) 
    return mylist
