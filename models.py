from flask_sqlalchemy import SQLAlchemy

#initialize the db
db = SQLAlchemy()

#product model

class Product (db.Model):
    __tablename__ = 'Product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Product {self.name}>"
    
    
        # Utility function to return product as a dict (for simplicity in this example)
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock
        }