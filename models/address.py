from db import db

class Address(db.Model):
    __tablename__ = 'restaurant_address'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    postal_code = db.Column(db.String(100), unique=False, nullable=True)
    street_address = db.Column(db.String(100), unique=False, nullable=True)
    address_locality = db.Column(db.String(100), unique=False, nullable=True)
    address_region = db.Column(db.String(100), unique=False, nullable=True)
    address_country = db.Column(db.String(100), unique=False, nullable=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)  

    def to_dict(self):
        return {
        'postalCode': self.postal_code,      
        'streetAddress': self.street_address,
        'addressLocality': self.address_locality,
        'addressRegion': self.address_region,
        'addressCountry': self.address_country
        }                    



    @classmethod
    def find_by_city(self, city):
        return db.session().query(Address).filter_by(address_locality=city)             
