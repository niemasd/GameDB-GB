#! /usr/bin/env python3
'''
Convert the GameID output of a GB game to its GameDB-GB folder name
'''

def clean(s):
    s = s.strip()
    for c in set(s):
        if not ('a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9'):
            s = s.replace(c, '_')
    return s

from sys import argv, stderr
if len(argv) == 1:
    from sys import stdin as f
elif len(argv) == 2:
    f = open(argv[1], 'rt')
else:
    print("USAGE: %s [GameID_output.txt]" % argv[0], file=stderr); exit(1)
data = dict()
for line in f:
    k, v = [x.strip() for x in line.strip().split('\t')]
    data[k] = v
print('.....'.join(clean(data[k]) for k in ['internal_title', 'global_checksum_expected']))
