from flask_restful import Api, Resource
from flask import request

from db import db
from ma import ma
api = Api()

from models.address import Address
from models.restaurant import Restaurant

from schemas.address import AddressSchema, address_schema, addresss_schema
from schemas.restaurant import RestaurantSchema, restaurant_schema, restaurants_schema

NOT_FOUND= "Restaurant not found."

class RestaurantListResource(Resource):
    def get(self):

        restaurants = Restaurant.query.all()
        
        if 'city' in request.args:      
            city = request.args.get('city')
            addresses = db.session().query(Address).filter_by(address_locality=city)
            restaurants = []
            for address  in addresses:
                restaurant = Restaurant.query.get_or_404(address.restaurant_id)
                restaurants.append(restaurant)                

        return restaurants_schema.dump(restaurants)


    def post(self):

        item_json = request.get_json()
        restaurant_data = restaurant_schema.load(item_json) #includes validation 
        db.session.add(restaurant_data)  
        db.session.commit()
        return restaurant_schema.dump(restaurant_data), 201 

api.add_resource(RestaurantListResource, '/api/restaurants')

class RestaurantResource(Resource):
    def get(self, restaurant_id):
        restaurant = Restaurant.query.get_or_404(restaurant_id) #returns 404 if not exists         
        return restaurant_schema.dump(restaurant), 200

    def put(self, restaurant_id):
        restaurant = Restaurant.query.get_or_404(restaurant_id) #returns 404 if not exists    

        if 'name' in request.json:
            restaurant.name = request.json['name']
        if 'url' in request.json:
            restaurant.url = request.json['url']
        if 'menu' in request.json:
            restaurant.menu = request.json['menu']
        if 'telephone' in request.json:
            restaurant.telephone = request.json['telephone']    
        if 'priceRange' in request.json:
            restaurant.price_range = request.json['priceRange']              
        if 'address' in request.json:
            address = db.session().query(Address).filter_by(restaurant_id= restaurant_id).first()
            address_data = request.json['address']
            if 'addressCountry' in address_data:
                address.address_country = address_data['addressCountry']
            if 'addressLocality' in address_data:
                address.address_locality = address_data['addressLocality']                 
            if 'addressRegion' in address_data:
                address.address_region = address_data['addressRegion']                                 
            if 'postalCode' in address_data:
                address.postal_code = address_data['postalCode']                                                 
            if 'streetAddress' in address_data:
                address.street_address = address_data['streetAddress']                                                                              
        
        db.session.commit()
        return restaurant_schema.dump(restaurant)

    def delete(self, restaurant_id):
        restaurant = Restaurant.query.get_or_404(restaurant_id) #returns 404 if not exists    
        db.session.delete(restaurant)
        db.session.commit()        
        return '', 204

api.add_resource(RestaurantResource, '/api/restaurants/<int:restaurant_id>')