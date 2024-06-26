def location_lat_long(place):
    """Returns the name of the location based on the latitude and longitude coordinates."""
    import pandas as pd
    df = pd.read_csv("datasets/places.csv")

    place = df[df["name"] == place ]
    long=place["longitude"].to_list()
    lat=place["latitude"].to_list()
    destination = (lat[0],long[0])
    return destination




print(location_lat_long("United Kingdom"))   
