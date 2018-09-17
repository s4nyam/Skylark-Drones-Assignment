import csv
globaldata = []
with open('latlon.csv') as csvfile:
	readCSV = csv.reader(csvfile,delimiter=',')
	# print(readCSV)
	for row in readCSV:
		print(row)
		print('lon = ' + (row[0]))
		print('lat = ' + (row[1]))
		# for each in row:
		# 	lon = int(row[0])
