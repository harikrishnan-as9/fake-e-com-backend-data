import os
import random
from models.category import CategoryModel
from models.product import ProductModel

# def populate():
#     electronics = CategoryModel(name='Electronics')
#     toys = CategoryModel(name='Toys')

#     electronics.save()
#     toys.save()

#     camera = ProductModel(name='camera'.capitalize(),price=random.randint(1, 10), stock=random.randint(0, 10),description='',rating=round(random.uniform(1,5),2),rated_by=random.randint(1, 100),category=electronics)
#     laptop = ProductModel(name='laptop'.capitalize(),price=random.randint(1, 10), stock=random.randint(0, 10),description='',rating=round(random.uniform(1,5),2),rated_by=random.randint(1, 100),category=electronics)
#     watch = ProductModel(name='watch'.capitalize(),price=random.randint(1, 10), stock=random.randint(0, 10),description='',rating=round(random.uniform(1,5),2),rated_by=random.randint(1, 100),category=electronics)

#     gun = ProductModel(name='gun'.capitalize(),price=random.randint(1, 10), stock=random.randint(0, 10),description='',rating=round(random.uniform(1,5),2),rated_by=random.randint(1, 100),category=toys)
#     waterbaloon = ProductModel(name='waterbaloon'.capitalize(),price=random.randint(1, 10), stock=random.randint(0, 10),description='',rating=round(random.uniform(1,5),2),rated_by=random.randint(1, 100),category=toys)
#     clay = ProductModel(name='clay'.capitalize(),price=random.randint(1, 10), stock=random.randint(0, 10),description='',rating=round(random.uniform(1,5),2),rated_by=random.randint(1, 100),category=toys)
#     lego = ProductModel(name='lego'.capitalize(),price=random.randint(1, 10), stock=random.randint(0, 10),description='',rating=round(random.uniform(1,5),2),rated_by=random.randint(1, 100),category=toys)

#     camera.save()
#     laptop.save()
#     watch.save()
#     gun.save()
#     waterbaloon.save()
#     clay.save()
#     lego.save()
    


def populate():
    folder = 'items/'
    items = os.listdir(folder)
    for item in items:
        path_name = folder+item
        category_name=item.split('.')[0].capitalize()
        category = CategoryModel(name=category_name.capitalize())
        category.save()
        file1 = open(path_name, 'r')
        Lines = file1.readlines()
        for line in Lines:
            product_name = line.strip()
            product = ProductModel(name=product_name.capitalize(),price=random.randint(1, 10), stock=random.randint(0, 10),description='',rating=round(random.uniform(1,5),2),rated_by=random.randint(1, 100),category=category)
            product.save()
