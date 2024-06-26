def get_names():
    import pandas as pd
    df = pd.read_csv("./places.csv")
    list_of_places = []
    for name in df["name"]:
        list_of_places.append(name)

    return list_of_places

print(get_names())
