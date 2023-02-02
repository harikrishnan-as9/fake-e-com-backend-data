from db import db

class CategoryModel(db.Model):
    __tablename__ = 'category_tbl'
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    products = db.relationship('ProductModel', backref='category')

    def json(self):
        return {
            '_id': self._id,
            'name': self.name,
            "image": 'https://picsum.photos/200',
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
