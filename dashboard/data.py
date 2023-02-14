"""this module contains data"""

import ast
import geopandas as gpd
from geopy.geocoders import Nominatim
from plotly import express as px

geocoder = Nominatim(user_agent='app')

us_houses_geo_df = gpd.read_file('../houses-data-shapefile/us-houses-shapefile.shp')
us_states_df = gpd.read_file('../usa-states-shapefile/cb_2018_us_state_500k.shp')

def get_average_price_by_state(state: str) -> float:
    """getting average house price in each state"""

    by_state = us_houses_geo_df.groupby('state')

    if state not in us_houses_geo_df['state'].unique():
        av_house_price = 0
    else:
        av_house_price = by_state.get_group(state)['price'].mean()

    return av_house_price


def plot_single_state_house_price(state: str):
    """plots single state plot for average house price"""

    lat = geocoder.geocode(state).latitude
    long = geocoder.geocode(state).longitude

    us_states_df['AVERAGE_HOUSE_PRICE'] = us_states_df['NAME'].apply(get_average_price_by_state)
    state_df = us_states_df[us_states_df['NAME']==state]
    geojson = ast.literal_eval(state_df[['GEOID', 'geometry']].to_json())

    fig = px.choropleth_mapbox(state_df, geojson=geojson, color="AVERAGE_HOUSE_PRICE",
                               locations="GEOID", featureidkey="properties.GEOID",
                               center={"lat": lat, "lon": long},
                               hover_data=['NAME', 'AVERAGE_HOUSE_PRICE'],
                               mapbox_style="carto-positron", zoom=5)

    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_layout(coloraxis_showscale=False)

    return fig
