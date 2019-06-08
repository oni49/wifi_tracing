#!/usr/bin/env python3

import math
import sys
import xml.etree.ElementTree as etree
from gmplot import gmplot
import subprocess
import os


def parse_gps_xml(path):
    gps_dict = {}
    print('trying to parse xml')
    tree = etree.parse(path)
    root = tree.getroot()
    print('entering xml parse')
    for child in root:
        try:
            mac = child.attrib['bssid']
            lat = child.attrib['lat'] 
            lon = child.attrib['lon']
            rssi = child.attrib['signal_dbm']            
            if mac != '00:00:00:00:00:00' and 'GP' not in mac:
                if mac not in gps_dict:
                    gps_dict[mac] = [(float(lat), float(lon), int(rssi))]
                elif mac in gps_dict:
                    gps_dict[mac].append((float(lat), float(lon), int(rssi)))
        except Exception as e:
            pass
    print('leaving parse_gps_xml')
    return gps_dict


def find_map_center(loc_list):
    temp_lat_list = []
    temp_lon_list = []
    for x in loc_list:
        temp_lat_list.append(x[0])
        temp_lon_list.append(x[1])
    # avg_lat = [gps_dict[key] for key in gps_dict for gps_dict[key] in key] # failed list comp
    return((sum(temp_lat_list)/len(temp_lat_list), min(temp_lat_list), max(temp_lat_list)) , (sum(temp_lon_list)/len(temp_lon_list), min(temp_lon_list), max(temp_lon_list)))


def make_map(mac, lat_list, lon_list, rssi_list):
    locs = zip(lat_list, lon_list, rssi_list)
    locs = list(locs) #cluge code to sidestep the zip iterable issue
    middle = find_map_center(locs)
    gmap = gmplot.GoogleMapPlotter(middle[0][0], middle[1][0], 15, apikey=os.environ["GOOGLE_API_KEY"])
    for loc in locs:
        rad = get_distance_rssi(loc[2])
        gmap.circle(loc[0], loc[1], rad/2, c='red', face_alpha=0.01)
    gmap.draw(''.join([x for x in mac.split(':')]) + '.html')


def draw_points(gps_dict):
    for key in gps_dict:       
        lat_list = []
        lon_list = [] 
        rssi_list = []
        for x in gps_dict[key]:
            lat_list.append(x[0])
            lon_list.append(x[1])
            rssi_list.append(x[2])
        make_map(key, lat_list, lon_list, rssi_list)


def get_distance_rssi(rssi, tx_pow=-20):
    '''
    RSSI = TxPower - 10 * n * lg(d)
    d = 10 ^ ((TxPower - RSSI) / (10 * n))
    n = 2 (in free space) - adjust based on GIS lookup
    '''
    # distance = math.pow(10, (tx_pow - rssi) / (10 * 2))
    distance = math.pow(10,-((rssi - tx_pow) /(10*2.7)))
    return distance


if __name__ == '__main__':
    xml_path = sys.argv[1]
    gps_dict = parse_gps_xml(xml_path)
    draw_points(gps_dict)
