from flask_restx import Namespace, Resource, fields 
from  models import db, Product

#initialize the product  namespace

product_ns = Namespace('products', description='operations related to products')

#Define a product model using flask-restx fields
product_model = product_ns.model(' Product',{
    'id':fields.Integer(readonly=True, description='The Unique identifier of a product'),
    'name':fields.String(readonly=True, description='The name of a product'),
    'price':fields.Float(readonly=True, description='The price of a product'),
    'stock':fields.Integer(readonly=True, description='The number of items available')
})

#product CRUD Resources
@product_ns.route('/')
class ProductList(Resource):
    def get(self):
        """List all the Products"""
        products = Product.query.all()
        return [product. as_dict() for product in products],200
    
    def post(self):
        """create a new product"""
        data = product_ns.payload
        new_product =  Product(
            name = data['name'],
            price = data['price'],
            stock = data['stock']
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product.as_dict(),201
    
@product_ns.route('/<int:id>')
class ProductResource(Resource):
    def get(self, id):
        """get a single product by id"""
        product = Product.query.get_or_404(id)
        return product.as_dict(),200
    
    def put(self,id):
        """update a product"""
        data = product_ns.payload
        product = Product.query.get_or_404(id)
        product.name = data['name']
        product.price = data['price']
        product.stock = data['stock']
        db.session.commit()
        return product.as_dict(),200
    
    def delete(self,id):
        """delete a product"""
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        return '',204   
        