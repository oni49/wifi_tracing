#!/usr/bin/env python

import time
from scapy.all import Dot11, sniff

#log = list( (mac, ssid, rssi, sensor, time) )
log = list()
log_file = open('wap.log', 'a+')
log_count = 0

#Sensor information
interface = "wlan1"
sensor_name = "Pi3B"
polling_time = 60 #time for polling in seconds
channel_hop_time = 5 #time to switch channels in seconds

def new_mac(mac):
        return True if mac not in [x[0] for x in log] else False

def new_ssid(mac, ssid):
        return True if (mac, ssid) not in [(x[0],x[1]) for x in log] else False

def new_time(mac):
        last_time = max([x[-1] for x in log if x[0] == mac])
        return True if (time.time() - last_time) > polling_time else False

def log_mac(mac, ssid, rssi, channel, sensor):
        global log_count
        log.append((mac, ssid, rssi, sensor, time.time()))
        log_file.write("{0},{1},{2},{3},{4},{5}\n".format(mac, ssid, rssi, channel, sensor, time.time()))
        log_count = (log_count + 1) % 10
        if log_count == 0:
                log_file.flush()

def PacketHandler(packet, channel):
        #if it's an 802.11 packet/frame
        if packet.haslayer(Dot11):
                if new_mac(packet.addr2) or new_ssid(packet.addr2, packet.info) or new_time(packet.addr2):
                	log_mac(packet.addr2, packet.info, 0, channel, sensor_name)

if __name__ == "__main__":
	import os

	os.system("ifconfig " + interface + " down")
	os.system("iwconfig " + interface + " mode monitor")
	os.system("ifconfig " + interface + " up")

	# Thanks to: https://gist.github.com/garyconstable/16b12823411c2d6515fb
	while True:
		for channel in range(1,14):
			#channel = x
			os.system("iwconfig " + interface + " channel " + str(channel))

			sniff(iface="wlan1", prn=lambda x: PacketHandler(x, channel), filter="type management and subtype beacon", store=0, timeout=channel_hop_time)
