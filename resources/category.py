from flask_restful import Resource
from models.category import CategoryModel

class Categories(Resource):
    def get(self):
        return [cat.json() for cat in CategoryModel.find_all()]


class Categorie(Resource):
    def get(self,_id):
        cat = CategoryModel.find_by_id(_id)
        if cat is None:
            return {
                'msg': 'no item found with that id'
            }, 404
        return cat.json()
            
