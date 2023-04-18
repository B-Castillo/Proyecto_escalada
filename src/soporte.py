
from geopy.geocoders import Nominatim
import numpy as np



def geo_cord(local):

    try:

        geoloca = Nominatim(user_agent= "brand")
        localizacion = geoloca.geocode(local)

        return localizacion.latitude, localizacion.longitude
    
    except:
        
        return np.nan
    
