from ma import ma
from marshmallow import Schema, fields, validate
from schemas.address import AddressSchema
from marshmallow_sqlalchemy import SQLAlchemySchema, SQLAlchemyAutoSchema

from models.restaurant import Restaurant

class RestaurantSchema(ma.SQLAlchemySchema):
    address = ma.Nested(AddressSchema())      
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'url', 'menu', 'telephone', 'price_range')
        include_relationships = True
        load_instance = True
        
    price_range = ma.Str(data_key="priceRange")
        
# class RestaurantSchema(Schema):
#     id = fields.Integer()
#     name = fields.Str(validate=validate.Length(min= 1, max= 250, error= "Insira um nome um nome"), required=True)                         
#     address = fields.Nested(AddressSchema())          
#     url = fields.Str()
#     menu = fields.Str()
#     telephone = fields.Str()
#     price_range = fields.Str(data_key="priceRange")

#     load_instance = True
#     include_relationships = True

restaurant_schema = RestaurantSchema()
restaurants_schema = RestaurantSchema(many=True)          
