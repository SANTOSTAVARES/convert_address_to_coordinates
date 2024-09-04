from geopy.geocoders import Nominatim
import pandas as pd

users = [
    {'nome': 'Ana', 'tipo_cliente': 'Casual', 'endereco': 'Avenida Vasconcelos Costa, 270, Uberlândia, MG'},
    {'nome': 'Maria', 'tipo_cliente': 'Casual', 'endereco': 'Avenida Presidente Médici, 1001, Uberlândia, MG'},
    {'nome': 'Fernanda', 'tipo_cliente': 'Casual', 'endereco': 'Avenida Getúlio Vargas, 450, Uberlândia, MG'},
    {'nome': 'Vanessa', 'tipo_cliente': 'Frequente', 'endereco': 'Avenida João Naves de Ávila, 999, Uberlândia, MG'},
    {'nome': 'Bia', 'tipo_cliente': 'Frequente', 'endereco': 'Avenida Seme Simão, 999, Uberlândia, MG'}
]

geolocator = Nominatim(user_agent= 'app.py', timeout= 10)
data_to_df = []
for user in users:
    
    location = geolocator.geocode(user['endereco'])
    
    try:
        user['latitude'] = location.latitude
        user['longitude'] = location.longitude
    except:
        user['latitude'] = None
        user['longitude'] = None
    data_to_df.append(user)

df = pd.DataFrame(data=data_to_df, 
                  columns=['nome', 'tipo_cliente', 
                           'endereco', 'latitude', 'longitude'])
