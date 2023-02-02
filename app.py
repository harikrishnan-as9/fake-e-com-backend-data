import os
from flask import Flask, render_template
from flask_restful import Api

from db import db
from resources.category import Categories, Categorie
from resources.product import Products, Product


app = Flask(__name__)

app.secret_key = 'thesecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random')
def random():
    db.drop_all()
    db.create_all()
    print('db creted')
    populate()
    print('populated')
    return render_template('regnerated.html')

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response

from populate import populate
@app.before_first_request
def before_first_request():
    db.drop_all()
    db.create_all()
    print('db creted')
    populate()
    print('populated')


api.add_resource(Categories, '/categories')
api.add_resource(Categorie,'/category/<int:_id>')
api.add_resource(Products, '/products')
api.add_resource(Product,'/product/<int:_id>')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
