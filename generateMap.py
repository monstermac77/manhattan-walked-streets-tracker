#!/usr/bin/python

# had to run:
# sudo apt-get update
# sudo apt-get install libgdal-dev
# pip install fiona

import fiona
import pprint

# keep this handy: https://streets.planning.nyc.gov/about?lat=-73.9634&lng=40.7743&zoom=17

city = fiona.open("citymap_citymap_v1/citymap_citymap_v1.shp")

#first feature of the shapefile
streets = []
for i in range(0,1000):
	element = city.next()
	
	# check if it's a street in Manhattan
	elementType = element['properties']['type']
	elementBorough = element['properties']['boro_nm']

	if elementType == "Mapped Street" and elementBorough == "Manhattan":
		streets.append(element)

pprint.pprint(streets)