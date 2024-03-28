from ma import ma
from marshmallow import Schema, fields, validate
from marshmallow_sqlalchemy import SQLAlchemySchema, SQLAlchemyAutoSchema

from models.address import Address

class AddressSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Address
        fields = ('postal_code', 'street_address', 'address_locality', 'address_region', 'address_country')
        include_relationships = True
        load_instance = True

    postal_code = fields.Str(data_key="postalCode", required=True)
    street_address = fields.Str(data_key="streetAddress", required=True)
    address_locality = fields.Str(data_key="addressLocality", required=True)    
    address_region = fields.Str(data_key="addressRegion", required=True)
    address_country = fields.Str(data_key="addressCountry", required=True)



# class AddressSchema(Schema):
#     postal_code = fields.Str(data_key="postalCode", required=True)
#     street_address = fields.Str(data_key="streetAddress", required=True)
#     address_locality = fields.Str(data_key="addressLocality", required=True)    
#     address_region = fields.Str(data_key="addressRegion", required=True)
#     address_country = fields.Str(data_key="addressCountry", required=True)
#     load_instance = True
#     include_relationships = True

address_schema = AddressSchema()
addresss_schema = AddressSchema(many=True)