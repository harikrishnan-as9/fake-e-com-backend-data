from flask_restful import Resource
from models.product import ProductModel

class Products(Resource):
    def get(self):
        return [product.json() for product in ProductModel.find_all()]


class Product(Resource):
    def get(self,_id):
        product = ProductModel.find_by_id(_id)
        if product is None:
            return {
                'msg': 'no item found with that id'
            }, 404
        return product.json()
            
