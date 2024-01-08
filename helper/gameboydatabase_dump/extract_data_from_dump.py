#! /usr/bin/env python3
'''
Extract data into game folders from a Game Boy Database dump
'''
from bs4 import BeautifulSoup
from datetime import datetime
from os import makedirs
from sys import argv

# main program
if __name__ == "__main__":
    if len(argv) != 2:
        print("USAGE: %s <gameboydatabase_dump.txt>" % argv[0]); exit(1)
    soup = BeautifulSoup(open(argv[1]).read(), 'html.parser')
    for game in soup.find_all('div', {'class':'comment-body'}):
        try:
            title = game.find_all('h3')[0].text.strip()
            data = game.find_all('span')[0].text.strip()
            serial = data.split()[0].strip()
            date = None
            if '(' in data:
                date_tmp = data.split('(')[1].split(')')[0].strip().lower()
                if date_tmp not in {'no date appears', 'unknown'}:
                    date = datetime.strptime(date_tmp, '%d/%m/%Y').strftime('%Y-%m-%d')
            game_path = '../../games/%s' % serial
            makedirs(game_path, exist_ok=True)
            for fn, s in [('title.txt',title), ('release_date.txt',date)]:
                if s is not None:
                    f = open('%s/%s' % (game_path,fn), 'w'); f.write('%s\n' % s); f.close()
        except Exception as e:
            print("ERROR: %s" % game); raise e
