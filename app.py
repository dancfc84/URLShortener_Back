
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from config.environment import db_URI

from flask_marshmallow import Marshmallow

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#Configuring it with flask
app.config["SQLALCHEMY_DATABASE_URI"] = db_URI

#removes a warning for an unused part of the library
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


print(app)

db = SQLAlchemy(app)

ma = Marshmallow(app)


#Import controllers here
from controllers import links


#Put routes here
app.register_blueprint(links.router, url_prefix="/api")