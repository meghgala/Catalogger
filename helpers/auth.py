
from Catalogger import app
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import firestore

cred = credentials.Certificate(app.config['FIRESTORE_KEY_PATH'])
firebase_admin.initialize_app(cred)

firestore_client = firestore.client()

def createBusiness(name,email...):
    