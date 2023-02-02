from db import db

class ProductModel(db.Model):
    __tablename__ = 'product_tbl'
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=10)
    description = db.Column(db.Text)
    rating = db.Column(db.Integer)
    rated_by = db.Column(db.Integer)
    cat_id = db.Column(db.Integer, db.ForeignKey('category_tbl._id'))

    def json(self):
        return {
            '_id': self._id,
            'name': self.name,
            "price": self.price,
            "stock": self.stock,
            "description": self.description,
            "rating": self.rating,
            "rated_by": self.rated_by,
            "cat_id": self.cat_id,
            "image": 'https://picsum.photos/200',
            "category": self.category.json(),
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.get(_id)

    @classmethod
    def find_all(cls):
        return cls.query.all()