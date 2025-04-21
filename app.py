from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db
from resources.product import product_ns


#initialize app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#intialize db
db.init_app(app)

#create tables
with app.app_context():
    db.create_all()

# Set up RESTX
api = Api(app)
api.add_namespace(product_ns)

#migrate db
migrate = Migrate(app,db)

if __name__ == '__main__':
    app.run(debug=True)