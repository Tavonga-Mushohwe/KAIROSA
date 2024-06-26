
def get_distance(destination):
    """Calculate the distance from home the shop and the shop address"""
    
    origin_lat =17.7469397
    origin_lng = 30.9831807 
    from geopy.distance import geodesic
    distance_km = geodesic((origin_lat,origin_lng),destination).km
    return distance_km

print(get_distance(destination=(7.896955368061427,7.471582606739162)))