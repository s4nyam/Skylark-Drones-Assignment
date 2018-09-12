from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import csv
m = Basemap(projection='mill',llcrnrlat=21,urcrnrlat=37,llcrnrlon=56,urcrnrlon=79,resolution='c')
m.drawcoastlines()
m.drawcountries()
m.drawstates()
# m.bluemarble()
m.fillcontinents(color='white',lake_color='#FFFFFF')
m.drawmapboundary(fill_color='#FFFFFF')
with open('latlon.csv') as csvfile:
	readCSV = csv.reader(csvfile,delimiter=',')
#print(readCSV)
	for row in readCSV:
		print(row)
		print('lon = ' + (row[0]))
		print('lat = ' + (row[1]))
		lon,lat = float(row[0]),float(row[1])
		x,y = m(lon,lat)
		m.plot(x,y,'ro')
		

plt.title("Drone Attacks in pak")
plt.show()
# lon,lat = 69.9,33.0333
# x,y = m(lon,lat)
# m.plot(x,y, 'ro')
# lon, lat = 71.5, 34.6833
# xpt,ypt = m(lon,lat)
# m.plot(xpt,ypt, 'go')
# plt.title("Geo Plotting")
# # plt.show()

