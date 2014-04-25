#!/usr/bin/env python

import re
import bfs
import sets
import os

#dictionary for links
popular = {}
visited = sets.Set()

WIKI_DIR = '/Users/kevinrankine/wikipedia-game/wiki/'

all_links = {}

def load_links():
    for x in os.listdir(WIKI_DIR):
        all_links[x] = bfs.extract_links(WIKI_DIR + x)
    return all_links

#only gets all links from one path, not sure how to traverse directory and run on each file
def load_dict():
    for x in all_links.keys()
        for y in x
            visited.add(y)
        for links in all_links:
            if all_links[x][0] in popular.keys():
                popular[all_links[x][0]] += 1; #update frequency of link
            else:
                popular[all_links[x].pop(0)] = 1; #add element to dictionary
        for z in all_links[x]:
            if z in visited:
                pass
            else:
                load_dict(z)

#returns key from dictionary with the most links
def most_links():
    load_links()
    load_dict()
    return (sorted(popular, key=popular.__getitem__, reverse=True))[0]

def link_frequency(link):
    try:
        print popular[link]
    except(Exception):
        print "Article not in dictionary"




