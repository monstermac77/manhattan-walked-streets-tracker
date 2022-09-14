#!/usr/bin/python

# had to run:
# sudo apt-get update
# sudo apt-get install libgdal-dev
# pip install fiona
# pip install scipy
# pip install geopandas

import pprint
import fiona
import geopandas as gpd
import numpy as np
import pandas as pd

from scipy.spatial import cKDTree
from shapely.geometry import Point

# keep this handy: https://streets.planning.nyc.gov/about?lat=-73.9634&lng=40.7743&zoom=17
# since most of what we'll be doing is finding distances to points, this will be most used and so lets switch to geopandas: https://gis.stackexchange.com/q/222315

# once we're ready for the entire thing, we can do this instead. But it takes too long to do during development.
# city = gpd.read_file("citymap_citymap_v1/citymap_citymap_v1.shp")

# filtering to a smaller number during development
city = fiona.open("citymap_citymap_v1/citymap_citymap_v1.shp")
streets = []
for i in range(0,1000):
	element = city.next()

	# check if it's a street in Manhattan
	elementType = element['properties']['type']
	elementBorough = element['properties']['boro_nm']

	if elementType == "Mapped Street" and elementBorough == "Manhattan":
		streets.append(element)

partialCity = gpd.GeoDataFrame.from_features(streets)
print partialCity
sys.exit(1)