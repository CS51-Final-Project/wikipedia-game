#!/usr/bin/env python

import re
import bfs
import sets
import os

#dictionary for popular links
popular = {}
#set that keeps track of visited links
visited = sets.Set()

#generate the correct path for any user
WIKI_DIR = os.path.abspath("../data") + "/"

#dictionary for holding all links for compressed dictionary
all_links = {}

#creates a compressed dictionary of solely articles with their links
def load_links():
    for x in os.listdir(WIKI_DIR): #for each article
        all_links[x.lower()] = bfs.extract_links(WIKI_DIR + x) #extract its links
    return all_links

#only gets all links from one path
def load_dict(dictionary):
    for key in dictionary.keys(): #loop for all keys in dictionary
        for link in dictionary[key]: 
            visited.add(link) #keep track of links we've visited
        for links in dictionary[key]:
            if links in popular.keys():
                popular[links] += 1; #update frequency of link if its already in dict
            else:
                popular[links] = 1; #add element to dictionary if its not
    return popular

#returns key from dictionary with the most links
def most_links(dictionary):
    load_dict(dictionary) #create a popular dictionary from the condensed dictionary
    return (sorted(popular, key=popular.__getitem__, reverse=True))[:3] #return the most popular

#finds the center of the wikipedia directory (article that links to the most pages)
def center(dictionary):
    center_dict = {} #initializes a center dictionary
    pages = os.listdir(WIKI_DIR) #grabs all articles
    counter = 1
    length = len(pages)
    for p in pages:
        print "{0}/{1} - {2} BFSed".format(counter, length, p) #prints to command line for progress check
        counter += 1
        center_dict[p] = len(bfs.BFS(p, wiki_dict = dictionary).keys()) #runs a BFS on each page and fills center dict with that page and the number of pages it reaches
    return sorted(center_dict, key = center_dict.__getitem__, reverse = True)[0] #returns the page with highest value

#returns all pages that reference a certain page
def where_referenced(link, dictionary):
    load_dict(dictionary) #loads popular dictionary
    references = sets.Set() #initializes a new set for references
    for key in popular.keys(): #for each page
        if link in key: #if it references the page of interest
            references.add(key) #add it to the list of references
    try:
        print "{0} is referenced on the following pages:".format(link)
        for page in references:
            print page #prints all references cleanly
        print "\n"
    except(Exception):
        print "Article not in dictionary"



