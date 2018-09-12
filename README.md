# Skylark-Drones-Assignment
This is the part of Skylark-Drones-Assignment-for-Recruitment-process I got in second week of september. 


Hello,



This repository is a part of Skylark-drones-assignment. It has 5 different approaches to visualize geo-spatial data of &quot;_Pakistan Drone Attacks (2004-17)_&quot;.

The Five parts are as follows:



# Pythonic NaiveWay using Jupyter:

Links reference:\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*



 for shape and vector files: [https://www.naturalearthdata.com/](https://www.naturalearthdata.com/)

 More about jupyter notebook to use jupyter output to web :

           https://jupyter-notebook.readthedocs.io

 Plotting : https://www2.eecs.berkeley.edu/Pubs/TechRpts/2018/EECS-2018-57.pdf



 Plotting documentation : https://matplotlib.org/api/



 Spatial Data Download | DIVA-GIS

  : http://www.diva-gis.org/gdata



 OCHA Pakistan - Humanitarian Data Exchange

 : https://data.humdata.org/dataset/pakistan-admin-level-4-boundaries



 Download Free Pakistan ArcGIS Shapefile Map Layers

 : http://www.mapcruzin.com/free-pakistan-arcgis-maps-shapefiles.htm

Python Libs used:\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*



 geopy

 csv

 matplotlib

 numpy

 Basemap

 jupyter-noteebok





Tutorial:\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

1. First install all dependencies using requirements.txt

run command :sudo pip install -r requirements.txt

2. You will need to install basemap library directly from the website and follow the procedure mentioned there.

URL = https://matplotlib.org/basemap/users/installing.html

3. After installing all the repos and libraries just straight forward to the pythonic code folder and run &quot;python basemap\_implementation.py&quot;

4.If you don&#39;t know you location coord then fetch using addresstolatlon.py file by entering your address.

5. Also read the pdf file as outcome.

6. main file is &quot;basemap\_implementation.py&quot;

**Pythonic naive approach utilizes Basemap and matplotlib to plot csv data.**



# Using Basic google maps and CSV data to plot on google maps editor online :

Creating own google maps and using iframe directly to the webpage tio embed the map. It&#39;s that easy.



  **Mapbox simple:**



First thing first. Convert CSV data to geojson online. Then check the accuracy of geoJSON on geojson.io . Then add dataset to mapbox. Edit the dataset (dataset is nothing but your geojson file). Finalize the dataset to Tilesets. Use the tileset in studio after choosing a template or either blank start!!

After having done with mapbox, publish and make it public(as per requirement)

Take the share code in &quot;share&quot; section of the mapbox.

After having a sample code which can get you the mapbox map using web. Now add marker/onClick action to the points on map. The basic documentation of mapbox-gl-js can fetch you that.

The Description will give you raw JSON. that can be stringified and formatted in a tabular representation.



#  Folium+leaflet+OSM+advanced Python (Pythonic way) :

Run in command line  : python app.py and you ll get an output file called &quot;Mapi.html&quot;

FOLIUM IS POWER TO VISUALIZATION IN PYTHON-LEAFLET INTEGRATION

Also Please install dependencies before running the app:

&quot;sudo pip install pandas&quot;    -           to read CSV file

&quot;sudo pip install folium&quot;      -         to gain leaflet.js power in python

folium builds on the data wrangling strengths of the Python ecosystem and the mapping strengths of the leaflet.js library. Manipulate your data in Python, then visualize it in on a Leaflet map via folium .



also install all the tools required for data science in python :

Numpy + Scipy + Matplotlib + plotly + pandas + jupyter + seaborn

----------------------OR-----------------------------------

                    Anaconda

#D3 + GEOJSON + TOPOJSON :

This is the tricky way to do. There are some prerequisites for the same:

1. D3.JS (d3js.org)
2. Geojson.io
3. Knowledge of JS
4. CSV to GEOJSON to TOPOJSON
5. READ THE DOCS!!!!

First thing first. Importing d3.js and topojson.js from d3js.org github repo and saved in folder.

Pakmap.js contains actual logic.

d3 documentation helps a lot. This is all about the GeoJSON or topoJSON you have. You have better data maps and data sets with lat long you have better visualization.

Topojson is more of like compressed version of huge GEOJSON files in layman words.



A geojson url: That I created

[http://geojson.io/#id=gist:samy280497/210606a793bfa107e60bab42597a8f6d&amp;map=6/30.921/68.873](http://geojson.io/#id=gist:samy280497/210606a793bfa107e60bab42597a8f6d&amp;map=6/30.921/68.873)

1. Find an appropriate GeoJSON.
2. Draw a map with d3.js by plotting features from the GeoJSON.
3. Get population data and fill landmass colors correlating with population metrics.
4. Add interaction. (Whether can be a popup box or a mouse hover information)

Append  scalable vector graphics parent to the body. We will add our map to as a sibling to the parent svg. There are two ways either append everything or add everything to queue. Appending is done using svg.append({/\*operation\*/}) or d3.queue()

[https://github.com/d3/d3/blob/master/API.md](https://github.com/d3/d3/blob/master/API.md)   -  D3 DOCS

svg.selectAll(&quot;.pin&quot;)
    .data(places)
  .enter().append(&quot;circle&quot;, &quot;.pin&quot;)
    .attr(&quot;r&quot;, 5)
    .attr(&quot;transform&quot;, function(d) {
      return &quot;translate(&quot; + projection([
        d.location.latitude,
        d.location.longitude
     ]) + &quot;)&quot;

   })



Places the pin on Coordinates mentioned in JSON. Remaining code is just for viewing pakistan geographically balanced. This is fetched from newplots.json

Thanks for Reading.

Sanyam Jain
