from flask import Flask

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

from Catalogger.views import auth
from Catalogger.views import product
app.register_blueprint(auth.mod)
app.register_blueprint(product.mod)
