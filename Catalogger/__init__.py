from flask import Flask

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

from SalesTrackerV2.views import auth
app.register_blueprint(auth.mod)
