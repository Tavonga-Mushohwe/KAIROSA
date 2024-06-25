
def make_csv():
    import random

    result = "latitude,longitude,category,"
    file = open("data.csv","w")
    
    for i in range(490):
        latitude = random.uniform(-90,90)
        longitude = random.uniform(-180,180)
        category = 1
        file.write( f"{latitude},{longitude},{category}\n")

    

make_csv()
