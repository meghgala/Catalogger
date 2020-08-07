
from Catalogger import app
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import firestore

cred = credentials.Certificate(app.config['FIRESTORE_KEY_PATH'])
firebase_admin.initialize_app(cred)

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

def createBusinessUserAccount(name,email_id, password,bname,category):
    #try:
        user = auth.create_user(
            display_name=bname,
            email=email_id,
            email_verified=True,
            password=password,
        )
        _,b_user = firestore_client.collection('businesses').add({
            'name': bname,
            'category':category,
            'ownedBy': user.uid
        })
        firestore_client.collection('users').document(user.uid).set({
            'name': name,
            'ownerOf': b_user.id
        })
        print(b_user.id)
        return user.uid
    #except:
    #    print("Error")
    #    return None

def loginUserAccount(email_id, password):
    #try:
        user = auth.signInWithEmailAndPassword(
            email=email_id,
            password=password
        )
        return user.uid
    #except:
    #    print("Error")
    #    return None
    
     