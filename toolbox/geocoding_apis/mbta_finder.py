"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
from pprint import pprint
import sys


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

def get_json():
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """

    print 'Type a location to find the nearest MBTA Station'
    inp = raw_input("> ")

    address_inp = {'address': inp}
    url = 'https://maps.googleapis.com/maps/api/geocode/json?' + urllib.urlencode(address_inp)
    
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)

    return response_data
    #pprint(response_data)


def get_lat_long():
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    response_data = get_json()

    if len(response_data["results"]) == 0:
        print 'Sorry, please try your search again or try refining it further.'
        sys.exit()

    print "Is %s correct?" %response_data["results"][0]["formatted_address"]
    print "Type Y or N"
    y_n = raw_input("> ")

    if y_n == 'Y' or y_n == 'y':
        return response_data["results"][0]["geometry"]["location"]
    else:
        if len(response_data["results"]) >= 2: 
            print "Is %s correct?" %response_data["results"][1]["formatted_address"]
            print "Type Y or N"
            y_n = raw_input("> ")
            if y_n == 'Y' or y_n == 'y':
                return response_data["results"][1]["geometry"]["location"]
            else:
                print 'Sorry, please try your search again or try refining it further.'
                sys.exit()
        else:
            print 'Sorry, please try a new search or refine your previous one.'
            sys.exit()


def get_nearest_station():
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """

    lat_long = get_lat_long()

    url_inp = {'api_key': 'wX9NwuHnZU2ToO7GmGR9uw', 'lat': lat_long['lat'], 'lon': lat_long['lng']}
    url = 'http://realtime.mbta.com/developer/api/v2/stopsbylocation?' + urllib.urlencode(url_inp) + '&format=json'

    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)

    dic_1 = response_data['stop']
    dic_2 = dic_1[0]
    
    if dic_2['parent_station_name'] != '':
        station_name = dic_2['parent_station_name']
    else:
        station_name = dic_2['stop_name']

    station_distance = dic_2['distance']

    print 'The nearest MBTA station is %s, and it is %s miles away.' % (station_name,station_distance[0:4])

if __name__ == '__main__':
    get_nearest_station()