""" this module contains geo related functions."""


from geopy.geocoders import Nominatim

GEOCODER = Nominatim(user_agent='app')

def get_latitude(location: str) -> float:
    """get latitude of location"""

    latitude = GEOCODER.geocode(location).latitude
    if latitude is None:
        return None
    return latitude


def get_longitude(location: str) -> float:
    """get longitude of location"""

    longitude = GEOCODER.geocode(location).longitude
    if longitude is None:
        return None
    return longitude
