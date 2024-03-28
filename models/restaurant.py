from db import db

class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    address = db.relationship('Address', backref='restaurant', uselist=False, cascade='all, delete-orphan', lazy="subquery")
    url = db.Column(db.String(100), unique=False, nullable=True)
    menu = db.Column(db.String(100), unique=False, nullable=True)
    telephone = db.Column(db.String(100), unique=False, nullable=True)
    price_range = db.Column(db.String(100), unique=False, nullable=True)

    def to_dict(self):
        return {
        'id': self.id,
        'name': self.name,      
        'url': self.url,
        'menu': self.menu,
        'telephone': self.telephone,
        'priceRange': self.price_range
        }

    def __init__(self, name, address, url, menu, telephone, price_range):
        self.name = name
        self.address = address
        self.url = url        
        self.menu = menu        
        self.telephone = telephone        
        self.price_range = price_range        

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    def insert(self,):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()