from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent= 'app.py')
location = geolocator.geocode("Rua João Balbino, 10, Uberlândia, MG")
print(location.latitude, location.longitude)

import sqlite3 

connection_obj = sqlite3.connect('database.db') 

cursor_obj = connection_obj.cursor() 

cursor_obj.execute( 
"""SELECT u.user_name, ut.user_type_name, a.address_description 
from user u
inner join user_type ut 
on u.user_id = ut.user_id
inner join address a 
on u.user_id = a.user_id
"""
) 

query = cursor_obj.fetchall()
#print(query)
connection_obj.close() 
