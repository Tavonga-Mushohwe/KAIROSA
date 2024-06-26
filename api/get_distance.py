import random
import geocoder
def calculate_distance(user_lat,user_lon,shop_address):
    """Calculate the distance from home the shop and the shop address"""
    try:
        shop_location = geocoder.geocode(shop_address)
        shop_lat = shop_location.latitude
        shop_lon = shop_location.longitude
        from geopy.distance import geodesic
        distance_km = geodesic((user_lat,user_lon),(shop_lat,shop_lon)).km
        return distance_km

    except:
        distance_km = random.randint(1,1000)
        return distance_km
        
# print(calculate_distance(-17.746966,30.983202,"Irene College"))

def get_distance(destination):
    """Calculate the distance from home the shop and the shop address"""
    
    origin_lat =17.7469397
    origin_lng = 30.9831807 
    from geopy.distance import geodesic
    distance_km = geodesic((origin_lat,origin_lng),destination).km
    return distance_km

print(get_distance(destination=(7.896955368061427,7.471582606739162)))