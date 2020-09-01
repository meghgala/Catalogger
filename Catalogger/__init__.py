from flask import Flask

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

from Catalogger.views import auth
from Catalogger.views import category
from Catalogger.views import home
from Catalogger.views import business
app.register_blueprint(auth.mod)
app.register_blueprint(category.mod)
app.register_blueprint(home.mod)
app.register_blueprint(business.mod)
