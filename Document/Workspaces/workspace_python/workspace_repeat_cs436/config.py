import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Create the Connexion application instance
swagger = connexion.App(__name__, specification_dir='./')

# Get the underlying Flask app instance
app = swagger.app

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="panuchaiAnywhere",
    password="3Or20t6X0yEAh",
    hostname="panuchaiAnywhere.mysql.pythonanywhere-services.com",
    databasename="panuchaiAnywhere$hotels",
)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['SQLALCHEMY_ECHO'] = True

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)
