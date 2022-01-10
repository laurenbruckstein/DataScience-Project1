import argparse
import collections
import csv
import json
import glob
import math
import os
import pandas
import re
import requests
import string
import sys
import time
import xml

from requests import get
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Bike():
    def __init__(self, baseURL, station_info, station_status):
        # initialize the instance
        self.baseURL = get('https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en', verify=False);

        self.station_infoURL = get(baseURL+'/station_information.json', verify=False);
        self.station_statusURL = get(baseURL+'/station_status.json', verify=False);

        self.station_info = json.loads(self.station_infoURL.content);
        self.station_status = json.loads(self.station_statusURL.content);
        #print(self.station_info);
        #print(self.station_status);
        pass

    def total_bikes(self):
        # return the total number of bikes available
        #USE SELF.station_status

        data = self.station_status['data']
        stations = data['stations']

        totalBikes = 0;
        for i in stations:
            totalBikes += i['num_bikes_available']

        return totalBikes;

    def total_docks(self):
        # return the total number of docks available
        data = self.station_status['data']
        stations = data['stations']

        totalDocks = 0;
        for i in stations:
            totalDocks += i['num_docks_available']

        return totalDocks;

    def percent_avail(self, station_id):
        # return the percentage of available docks
        data = self.station_status['data']
        stations = data['stations']

        found = 0;
        for i in stations:
            curId = i['station_id']
            if str(curId) == str(station_id):
                found = 1
                numDocks = i['num_docks_available']
                numBikes = i['num_bikes_available']

        if found != 1:
            return ''

        #print(numDocks)
        #print(numBikes)
        total = numDocks/(numDocks+numBikes);
        total = total*100
        #print(total)
        return str(int(total)) + '%'

    def closest_stations(self, latitude, longitude):
        # return the stations closest to the given coordinates
        data = self.station_info['data']
        stations = data['stations']

        distList = []
        for i in stations:
            dist = self.distance(latitude, longitude, i['lat'], i['lon'])
            id = i['station_id']
            name = i['name']
            tup = (dist, id, name)
            #print(tup)
            distList.append(tup)
        distList.sort(key = lambda x: x[0])
        #print(distList);
        dict = {}
        for i in distList[0:3]:
            dict[i[1]] = i[2]
        #print(dict)
        return dict

            #given lat and long compute distance with distance function
            #create a tuple of 3 elements (dist, id, name)
            #add new tuple into list each time you create
            #add tuples into a list and sort list

    def closest_bike(self, latitude, longitude):
        # return the station with available bikes closest to the given coordinates

        #GET CLOSEST COORDS
        data = self.station_info['data']
        stations = data['stations']

        distList = []
        for i in stations:
            dist = self.distance(latitude, longitude, i['lat'], i['lon'])
            id = i['station_id']
            name = i['name']
            tup = (dist, id, name)
            #print(tup)
            distList.append(tup)
        distList.sort(key = lambda x: x[0])

        #CHECK IF CLOSEST COORDS HAVE BIKES AVALIABLE
        data = self.station_status['data']
        stations = data['stations']
        #print(distList)

        dict = {}

        for i in distList:
            for j in stations:
                if len(dict) == 1:
                    break;
                if i[1] == j['station_id']:
                    if j['num_bikes_available'] > 0:
                        dict[i[1]] = i[2]
        #print(dict)
        return dict

    def station_bike_avail(self, latitude, longitude):
        # return the station id and available bikes that correspond to the station with the given coordinates

        data = self.station_info['data']
        stations = data['stations']

        station_id = 0
        for i in stations:
            curlat = i['lat']
            curlon = i['lon']
            if curlat == latitude and curlon == longitude:
                station_id = i['station_id']

        dictResult = {}
        if station_id == 0:
            return dictResult

        data = self.station_status['data']
        stations = data['stations']

        for i in stations:
            if i['station_id'] == station_id:
                bikes = i['num_bikes_available']
                dictResult[station_id] = bikes

        return dictResult


    def distance(self, lat1, lon1, lat2, lon2):
        p = 0.017453292519943295
        a = 0.5 - math.cos((lat2-lat1)*p)/2 + math.cos(lat1*p)*math.cos(lat2*p) * (1-math.cos((lon2-lon1)*p)) / 2
        return 12742 * math.asin(math.sqrt(a))


# testing and debugging the Bike class

if __name__ == '__main__':
    instance = Bike('https://api.nextbike.net/maps/gbfs/v1/nextbike_pp/en', '/station_information.json', '/station_status.json')
    print('------------------total_bikes()-------------------')
    t_bikes = instance.total_bikes()
    print(type(t_bikes))
    print(t_bikes)
    print()

    print('------------------total_docks()-------------------')
    t_docks = instance.total_docks()
    print(type(t_docks))
    print(t_docks)
    print()

    print('-----------------percent_avail()------------------')
    p_avail = instance.percent_avail(342885) # replace with station ID
    print(type(p_avail))
    print(p_avail)
    print()

    print('----------------closest_stations()----------------')
    c_stations = instance.closest_stations(40.444618, -79.954707) # replace with latitude and longitude
    print(type(c_stations))
    print(c_stations)
    print()

    print('-----------------closest_bike()-------------------')
    c_bike = instance.closest_bike(40.444618, -79.954707) # replace with latitude and longitude
    print(type(c_bike))
    print(c_bike)
    print()

    print('---------------station_bike_avail()---------------')
    s_bike_avail = instance.station_bike_avail(40.438761, -79.997436) # replace with exact latitude and longitude of station
    print(type(s_bike_avail))
    print(s_bike_avail)
