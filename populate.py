import os
import random
from models.category import CategoryModel
from models.product import ProductModel
from faker import Faker
fake = Faker()
from config import config
    
def get_des(num=3):
    text = ''
    while num>0:
        num = num-1
        text += fake.text()
    text = text.replace('\r\n','')
    text = text.replace('\n','')
    return text

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
            des = get_des(
                random.randint(config['description_length_min'],config['description_length_min'])
                )
            product = ProductModel(
                name=product_name.capitalize(),
                price=random.randint(config['price_min'], config['price_max']), 
                stock=random.randint(config['stock_min'], config['stock_max']),
                description=des,
                rating=round(random.uniform(config['rating_min'], config['rating_max']),2),
                rated_by=random.randint(config['rated_by_min'], config['rated_by_max']),
                category=category
            )
            product.save()
