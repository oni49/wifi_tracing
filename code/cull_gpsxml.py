#!/usr/bin/env python3

import sys
import os


def cull_lines(path):
    lines = open(path, encoding='latin-1').readlines()
    out = []
    for line in lines:
        if 'GP' not in line and '00:00' not in line:
            out.append(line)
    # return [x for x in lines if 'GP' not in x and '00:00:00' not in x]
    return out


def write_file(contents):
    w_hand = open(name + '-culled.' + ext, 'w')
    w_hand.write(''.join(out_lines))
    w_hand.close()


if __name__ == '__main__':
    path = sys.argv[1]
    base = os.path.basename(path)
    try:
        name, ext = base.split('.')
    except:
        name = base
    out_lines = cull_lines(path)
    write_file(out_lines)
