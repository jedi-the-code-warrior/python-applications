# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 13:47:46 2019

@author: Anjani K Shiwakoti

Synopsis: Given starting address and destination address, calculate the geodesic 
distance between the two locations. A geodesic line is the shortest path between 
two points on a curved surface, like the Earth.
    
"""

from geopy.geocoders import Nominatim
from geopy.distance import geodesic

global location 
global geolocator

geolocator = Nominatim(user_agent="my_geo_location_tracker")

def getCoordinates(address):
    location = geolocator.geocode(address)

    #print(location.raw)
    #{'place_id': '9167009604', 'type': 'attraction', ...}
    
    return (location.latitude, location.longitude)

def getAddress(address):
    location = geolocator.geocode(address)

    return location.address


def getDistance(pointA, pointB):
    
    starting_coords = getCoordinates(pointA)
    destination_coords = getCoordinates(pointB)
    
    return (geodesic(starting_coords, destination_coords).miles)

starting_address = input("Enter Your Starting Address: ")
destination_address = input("Enter Your Destination Address: ")


print ("Your total geodesic distance between: ", 
       getAddress(starting_address), " and ", 
       getAddress(destination_address), " is: ",
       getDistance(starting_address, destination_address), "miles")
#print ("Your full address is: ", getCoordinates(starting_address)[0])
#print ("Your co-ordinates are: ", getCoordinates(starting_address)[1])

