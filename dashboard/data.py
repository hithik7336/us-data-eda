"""this module contains data"""

import geopandas as gpd
from plotly import graph_objs as go
from plotly import express as px

us_houses_geo_df = gpd.read_file('../houses-data-shapefile/us-houses-shapefile.shp')
us_states_df = gpd.read_file('../usa-states-shapefile/cb_2018_us_state_500k.shp')

def get_average_price_by_state(state):
    """getting average house price in each state"""
    
    by_state = us_houses_geo_df.groupby('state')
    
    if state not in us_houses_geo_df['state'].unique():
        av_house_price = 0
    else:
        av_house_price = by_state.get_group(state)['price'].mean()

    return av_house_price


def single_state_house_price(state: str) -> go.figure.Figure:
    """plots single state plot for average house price"""
    pass
     