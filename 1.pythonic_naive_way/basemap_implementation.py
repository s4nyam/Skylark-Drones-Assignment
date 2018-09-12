from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import csv
m = Basemap(projection='mill',llcrnrlat=21,urcrnrlat=37,llcrnrlon=56,urcrnrlon=79,resolution='c')
m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.bluemarble()
print("Welcome to Pak Drone Attacks Geo Visualization in Python")
#asking user if want to add data????? ;)
z = raw_input("Do You Want to add location data or go over directly type y of n:   ")
if(z == 'y'):
	print("Enter longitude and latitude you know where Drone Attacks in Pakistan held: (User data will be shown in blue color)")
	userLon = raw_input("Enter Longitude:")
	userLat = raw_input("Enter Latitude:")
	userlon,userlat = float(userLon),float(userLat)
	userX,userY = m(userlon,userlat)
	m.plot(userX,userY,'bo')
	plt.title("Drone Attacks in pak")
	plt.show()

else:

	#     m.fillcontinents(color='#04BAE3',lake_color='#FFFFFF')
	#   m.drawmapboundary(fill_color='#FFFFFF')
	with open('latlon.csv') as csvfile:
		readCSV = csv.reader(csvfile,delimiter=',')
	#print(readCSV)
		for row in readCSV:
			print(row)
			print('lon = ' + (row[0]))
			print('lat = ' + (row[1]))
			lon,lat = float(row[0]),float(row[1])
			x,y = m(lon,lat)
			m.plot(x,y,'r.')
			

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

