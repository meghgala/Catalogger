import os
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(24)
    
    DB_PATH = 'SalesTrackerV2/static/master.db'
    IMAGE_UPLOADS = 'SalesTrackerV2/static/Products/'
    IMAGE_THUMBNAIL_UPLOADS = 'SalesTrackerV2/static/Products_Thumbnails/'
    ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG"]
    FIRESTORE_KEY_PATH = 'Catalogger/static/catalogger-key'


class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.urandom(24)
    
    DB_PATH = 'SalesTrackerV2/static/master.db'
    IMAGE_UPLOADS = 'SalesTrackerV2/static/Products/'
    IMAGE_THUMBNAIL_UPLOADS = 'SalesTrackerV2/static/Products_Thumbnails/'
    ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG"]

    FIRESTORE_KEY_PATH = 'Catalogger/static/catalogger-key'



class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = os.urandom(24)
    DB_PATH = 'SalesTrackerV2/static/master.db'
    IMAGE_UPLOADS = 'SalesTrackerV2/static/Products/'
    IMAGE_THUMBNAIL_UPLOADS = 'SalesTrackerV2/static/Products_Thumbnails/'
    ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG"]
    FIRESTORE_KEY_PATH = 'Catalogger/static/catalogger-key'


# DB_NAME = "development-db"
# DB_USERNAME = "admin"
# DB_PASSWORD = "example"