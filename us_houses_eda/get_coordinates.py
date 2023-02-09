"""this module contains functions for getting coordinates of a place"""


from geopy.geocoders import Nominatim

GEOCODER = Nominatim(user_agent='app')

def get_latitude(location: str) -> float:
    """get latitude of location"""

    geocode = GEOCODER.geocode(location)
    if geocode is None:
        latitude = None
    else:
        latitude = geocode.latitude
    return latitude


def get_longitude(location: str) -> float:
    """get longitude of location"""

    geocode = GEOCODER.geocode(location)
    if geocode is None:
        longitude = None
    else:
        longitude = geocode.longitude
    return longitude
