#!/usr/bin/env python3

import xml.etree.ElementTree as etree
import sys
import hashlib
import os


def create_hash(mac, secret_key):
    return hashlib.md5((mac+secret_key).encode('UTF-8')).hexdigest()


def sanitize_xml(path, secret_key):
    file_name, ext = os.path.basename(path).split('.')
    print('trying to parse xml')
    tree = etree.parse(path)
    root = tree.getroot()
    print('entering xml parse')
    for child in root:
        try:
            mac = child.attrib['bssid']
            source = child.attrib['source']
            ha_mac = create_hash(mac, secret_key)
            ha_src = create_hash(source, secret_key)
            child.attrib['bssid'] = ha_mac
            child.attrib['source'] = ha_src
        except Exception as e:
            pass
    print('leaving parse_gps_xml')
    tree.write(file_name + '-sanitized.' + ext)


if __name__ == '__main__':
    path = sys.argv[1]
    secret_key = open("key_file.txt", 'r').read()
    sanitize_xml(path, secret_key)