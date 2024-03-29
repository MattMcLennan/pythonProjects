import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    return 'red'


map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="MyMap")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[
        lt, ln], popup=str(el)+" m", radius=6, fill_color=color_producer(el), color="grey", fill_opacity=0.7))

map.add_child(fg)

map.save("Map1.html")
