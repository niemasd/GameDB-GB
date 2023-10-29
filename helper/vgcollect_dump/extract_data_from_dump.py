#! /usr/bin/env python3
'''
Extract data into game folders from a VGCollect dump
'''
from json import load as jload
from os import makedirs
from sys import argv

# main program
if __name__ == "__main__":
    if len(argv) != 2:
        print("USAGE: %s <vgcollect_dump.json>" % argv[0]); exit(1)
    data = jload(open(argv[1]))
    for serial in data:
        game_path = '../../games/%s' % serial
        makedirs(game_path, exist_ok=True)
        for k in data[serial]:
            f = open('%s/%s.txt' % (game_path, k), 'w'); f.write('%s\n' % data[serial][k]); f.close()
