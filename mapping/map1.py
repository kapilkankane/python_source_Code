import folium as fl
import pandas as pd

map = fl.Map(location=[38.58,-99.99], zoom_start=6, tiles="Stamen Terrain")

data = pd.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])

coordinates = list(zip(lat,lon))


fg = fl.FeatureGroup(name="My Map")
i = 1
for coordinate in coordinates:
    fg.add_child(fl.Marker(location=coordinate, popup=f"Hi! I am a marker {i}", icon=fl.Icon(color='green')))
    i+=1

map.add_child(fg)

map.save("Map1.html")
