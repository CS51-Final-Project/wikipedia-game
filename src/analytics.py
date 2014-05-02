#!/usr/bin/env python

import re
import bfs
import sets
import os

#dictionary for links
popular = {}
visited = sets.Set()

WIKI_DIR = '/Users/kevinrankine/Repos/wikipedia-game/wiki/'

all_links = {}

def load_links():
    for x in os.listdir(WIKI_DIR):
        x = WIKI_DIR + x
        all_links[x] = bfs.extract_links(x)
    return all_links

#only gets all links from one path
def load_dict(dictionary):
    for key in dictionary.keys(): #loop for all keys in dictionary
        for link in dictionary[key]: #keep track of links we've visited
            visited.add(link)
        for links in dictionary[key]:
            if links in popular.keys():
                popular[links] += 1; #update frequency of link
            else:
                popular[links] = 1; #add element to dictionary
    return popular

#returns key from dictionary with the most links
def most_links(dictionary):
    load_dict(dictionary) #create a popular dictionary from the condensed dictionary
    return (sorted(popular, key=popular.__getitem__, reverse=True))[0] #return the most popular

def link_frequency(link, dictionary):
    load_dict(dictionary)
    try:
        print "{0} is referenced {1} number of times".format(link, popular[link])
    except(Exception):
        print "Article not in dictionary"

def center():
    center_dict = {}
    pages = os.listdir(WIKI_DIR)
    for p in pages:
        center_dict[p] = len(bfs.BFS(p).keys())
    return sorted(center_dict, key = center_dict.__getitem__, reverse = True)[0]

def where_referenced(link, dictionary):
    try:
        print "{0} is referenced on the following pages: \n {1}".format(link, dictionary[link])
    except(Exception):
        print "Article not in dictionary"



