#! /usr/bin/env python3
'''
Try to add missing regions
'''
from glob import glob
from os.path import isfile
REGION = {
    'ASI': 'NTSC-J',
    'AUS': 'PAL',
    'CAN': 'NTSC-U',
    'CHN': 'NTSC-J',
    'ESP': 'PAL',
    'EUR': 'PAL',
    'EUU': 'PAL',
    'FAH': 'PAL',
    'FRA': 'PAL',
    'FRG': 'PAL',
    'GPS': 'PAL',
    'HOL': 'PAL',
    'ITA': 'PAL',
    'JPN': 'NTSC-J',
    'KOR': 'NTSC-J',
    'NOE': 'PAL',
    'SCN': 'PAL',
    'TWN': 'NTSC-J',
    'UKV': 'PAL',
    'USA': 'NTSC-U',
}

# main program
if __name__ == "__main__":
    for folder in glob('*-*'):
        region_file = '%s/region.txt' % folder
        if not isfile(region_file):
            tmp = folder.split('-')[-1].strip().upper()
            if len(tmp) == 3:
                region = REGION[tmp]
                f = open(region_file, 'w'); f.write('%s\n' % region); f.close()
