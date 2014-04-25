#!/usr/bin/env python

import re
import bfs
import sets
import os

#dictionary for links
popular = {}
visited = sets.Set()

WIKI_DIR = '/Users/kevinrankine/wikipedia-game/wiki/'


#only gets all links from one path, not sure how to traverse directory and run on each file
def load_dict():
    for x in os.listdir(WIKI_DIR):
        links_to_follow = links = bfs.extract_links(WIKI_DIR + x)
        for x in links:
            visited.add(WIKI_DIR + x)
        while len(links) > 0:
            if links[0] in popular.keys():
                popular[links[0]] += 1; #update frequency of link
            else:
                popular[links.pop(0)] = 1; #add element to dictionary
        for x in links_to_follow:
            if x in visited:
                pass
            else:
                load_dict(x)

#returns key from dictionary with the most links
def most_links():
    load_dict()
    return (sorted(popular, key=popular.__getitem__, reverse=True))[0]

def link_frequency(link):
    try:
        print popular[link]
    except(Exception):
        print "Article not in dictionary"




