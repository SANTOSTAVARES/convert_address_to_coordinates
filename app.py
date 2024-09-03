import sqlite3 
from geopy.geocoders import Nominatim
import pandas as pd

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
users = cursor_obj.fetchall()
connection_obj.close() 

geolocator = Nominatim(user_agent= 'app.py', timeout= 10)
data_to_df = []
for user in users:
    user = list(user)
    location = geolocator.geocode(user[2])
    try:
        user.append(location.latitude)
        user.append(location.longitude)
    except:
        user.append(None)
        user.append(None)
    data_to_df.append(user)

df = pd.DataFrame(data=data_to_df, 
                  columns=['user_name', 'user_type_name', 
                           'address_description', 'latitude', 'longitude'])
