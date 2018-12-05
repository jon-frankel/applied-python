GOOGLE_API_KEY = 'AIzaSyDttiQ5XjbJAombW2oliPDujDtBw6XZD7Q'

import googlemaps
client = googlemaps.Client(key=GOOGLE_API_KEY)

def get_location(address):
    return client.geocode(address)
