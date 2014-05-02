#!/usr/bin/env python

import re
import bfs
import sets
import os

#dictionary for links
popular = {}
visited = sets.Set()

WIKI_DIR = os.path.abspath("../data") + "/"
all_links = {}

def load_links():
    for x in os.listdir(WIKI_DIR):
        all_links[x.lower()] = bfs.extract_links(WIKI_DIR + x)
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
    return (sorted(popular, key=popular.__getitem__, reverse=True))[:3] #return the most popular


def center(dictionary):
    center_dict = {}
    pages = os.listdir(WIKI_DIR)
    counter = 1
    length = len(pages)
    for p in pages:
        print "{0}/{1} - {2} BFSed".format(counter, length, p)
        counter += 1
        center_dict[p] = len(bfs.BFS(p, wiki_dict = dictionary).keys())
    return sorted(center_dict, key = center_dict.__getitem__, reverse = True)[0]

def where_referenced(link, dictionary):
    load_dict(dictionary)
    references = sets.Set()
    for key in popular.keys():
        if link in key:
            references.add(key)
    try:
        print "{0} is referenced on the following pages: \n {1}".format(link, references)
    except(Exception):
        print "Article not in dictionary"



