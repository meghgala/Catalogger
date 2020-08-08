import os
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(24)
    
    DB_PATH = 'SalesTrackerV2/static/master.db'
    IMAGE_UPLOADS = 'SalesTrackerV2/static/Products/'
    IMAGE_THUMBNAIL_UPLOADS = 'SalesTrackerV2/static/Products_Thumbnails/'
    ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG"]
    FIRESTORE_KEY_PATH = 'Catalogger/static/catalogger-key.json'
    DB_CONFIG = {
        "apiKey": "AIzaSyCvfS9pbQotKpJVtG3nrtIRgChnh99lX4U",
        "authDomain": "catalogger-68d96.firebaseapp.com",
        "databaseURL": "https://catalogger-68d96.firebaseio.com",
        "storageBucket": "catalogger-68d96.appspot.com",
    }


class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.urandom(24)
    DB_CONFIG = {
        "apiKey": "AIzaSyCvfS9pbQotKpJVtG3nrtIRgChnh99lX4U",
        "authDomain": "catalogger-68d96.firebaseapp.com",
        "databaseURL": "https://catalogger-68d96.firebaseio.com",
        "storageBucket": "catalogger-68d96.appspot.com",
    }
    DB_PATH = 'SalesTrackerV2/static/master.db'
    IMAGE_UPLOADS = 'SalesTrackerV2/static/Products/'
    IMAGE_THUMBNAIL_UPLOADS = 'SalesTrackerV2/static/Products_Thumbnails/'
    ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG"]

    FIRESTORE_KEY_PATH = 'Catalogger/static/catalogger-key.json'



class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = os.urandom(24)
    DB_PATH = 'SalesTrackerV2/static/master.db'
    IMAGE_UPLOADS = 'SalesTrackerV2/static/Products/'
    IMAGE_THUMBNAIL_UPLOADS = 'SalesTrackerV2/static/Products_Thumbnails/'
    ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG"]
    FIRESTORE_KEY_PATH = 'Catalogger/static/catalogger-key.json'
    DB_CONFIG = {
        "apiKey": "AIzaSyCvfS9pbQotKpJVtG3nrtIRgChnh99lX4U",
        "authDomain": "catalogger-68d96.firebaseapp.com",
        "databaseURL": "https://catalogger-68d96.firebaseio.com",
        "storageBucket": "catalogger-68d96.appspot.com",
    }


# DB_NAME = "development-db"
# DB_USERNAME = "admin"
# DB_PASSWORD = "example"