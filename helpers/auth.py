
from Catalogger import app
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import firestore

cred = credentials.Certificate(app.config['FIRESTORE_KEY_PATH'])
firebase_admin.initialize_app(cred)

firestore_client = firestore.client()

def createStudentAccount(name, email_id, password, bname, category, own):
    user = auth.create_user(
        display_name=name,
        email=email_id,
        email_verified=True,
        password=password,
        business_name = bname,
        category = category,
        owner = own
    )
    firestore_client.collection('businesses').document(user.uid).set({
        'name': name,
        'business name': bname,
        'category': category,
        'owenedBy': own,
        'uid': user.uid
    })
    print("Created user", user.uid)
    return user.uid
     
    
     