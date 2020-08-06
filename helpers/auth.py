
from Catalogger import app
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import firestore

cred = credentials.Certificate(app.config['FIRESTORE_KEY_PATH'])
firebase_admin.initialize_app(cred)

firestore_client = firestore.client()

def createStudentAccount(name, email_id, password="pass@123"):
    user = auth.create_user(
        display_name=name,
        email=email_id,
        email_verified=True,
        password=password
    )
    firestore_client.collection('businesses').document(user.uid).set({
        'name': name,
        'uid': user.uid
    })
    print("Created user", user.uid)
    return user.uid
     
    
     