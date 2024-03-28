DROP TABLE IF EXISTS restaurant;
DROP TABLE IF EXISTS restaurant_address;

CREATE TABLE restaurant (
    id INTEGER PRIMARY KEY,
    name TEXT, 
    url TEXT, 
    menu TEXT, 
    telephone TEXT, 
    price_range TEXT    
);

CREATE TABLE restaurant_address (
    id INTEGER PRIMARY KEY,
    restaurant_id INTEGER, 
    postal_code TEXT, 
    street_address TEXT, 
    address_locality TEXT, 
    address_region TEXT,
    address_country TEXT,
    FOREIGN KEY (restaurant_id) references restaurant(id)
);