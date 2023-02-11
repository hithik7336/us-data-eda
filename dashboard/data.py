"""this module contains data"""

import geopandas as gpd

us_houses_geo_df = gpd.read_file('../houses-data-shapefile/us-houses-shapefile.shp')
us_states_df = gpd.read_file('../usa-states-shapefile/cb_2018_us_state_500k.shp')
