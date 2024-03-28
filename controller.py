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
    def get(self,):

        restaurants = Restaurant.get_all()
                
        if 'city' in request.args:      
            city = request.args.get('city')            
            addresses = Address.find_by_city(city)
            restaurants = []
            for address  in addresses:                
                restaurant = Restaurant.find_by_id(address.restaurant_id)
                restaurants.append(restaurant)                
        return restaurants_schema.dump(restaurants)


    def post(self):

        item_json = request.get_json()
        try:
            restaurant_data = restaurant_schema.load(item_json) 
        except:
            return {'message': "Missing a required data"}, 400

        try:
            Restaurant.insert(restaurant_data)
            return restaurant_schema.dump(restaurant_data), 201 
        except:
            return {'message': "Internal Error"}, 500

api.add_resource(RestaurantListResource, '/api/restaurants')

class RestaurantResource(Resource):
    def get(self, restaurant_id):
        restaurant = Restaurant.find_by_id(restaurant_id)
        if restaurant:
            return restaurant_schema.dump(restaurant), 200
        return {'message': NOT_FOUND}, 404

    def put(self, restaurant_id):
        restaurant = Restaurant.find_by_id(restaurant_id)
        if not restaurant:
            return {'message': NOT_FOUND}, 404

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
        restaurant = Restaurant.find_by_id(restaurant_id)
        if not restaurant:
            return {'message': NOT_FOUND}, 404
        restaurant = Restaurant.remove(restaurant)        
        return '', 204

api.add_resource(RestaurantResource, '/api/restaurants/<int:restaurant_id>')