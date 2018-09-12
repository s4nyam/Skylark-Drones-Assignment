
# DONT KNOW WHATS THE ERROR

# -*- coding: utf-8 -*-
import folium
import pandas
data = pandas.read_csv("new.csv")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
print lat,lon  #todebug
html = """<h4>Pak Drone Attacks using folium - sanyam ;)</h4>
      %s m <br>Thanks!
"""

map = folium.Map(location=[30.18, 70.09], zoom_start=5, tiles="Mapbox Bright", max_zoom = 4)
fgv = folium.FeatureGroup(name="pak drone attacks")
for lt, ln in zip(lat, lon):
    iframe = folium.IFrame(html=html, width=200,height=100)
    fgv.add_child(folium.CircleMarker(location=[float(lt), float(ln)], radius = 6, popup=folium.Popup(iframe)))


    # if(float(lt) ,float(ln) == null):
    #     continue
     # I DONT KNOW WHY THIS IS NOT CONTINUING WITH NULL VALUE;
     # Dear Compiler please move on against null value FOR the sake of mother god
     # Actually db.cv is having null values in last thats y its reading those last null cells

########SANYAM JAIN WAS HERE


    # fill_color=color_producer(1000), fill=True,  color = 'grey', fill_opacity=0.7))
    


fgp = folium.FeatureGroup(name="City")
fgp.add_child(folium.GeoJson(data=open('map.json', 'r').read(),style_function=lambda x: {'fillColor':'red'}))
map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save(outfile="Mapi.html")

