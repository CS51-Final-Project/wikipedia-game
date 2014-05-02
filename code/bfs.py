#!/usr/bin/env python

import re
import os
import sets
import analytics

visited = sets.Set([]) # keeps track of whether we've visited a page yet
prev = {} # dictionary where (k, v) means to get to k we come from v
WIKI_DIR = os.path.abspath("../data") +"/" # the path of the wikipedia directory

'''
Extracts all the relevant links from a file given by "path"
'''
def extract_links(path):
    text = open(path).read() # open the file for reading
    pat = re.compile('<a href=[\'"]?([^\'" >]+)') # regexp for link urls
    
    links = re.findall(pat, text) # find the links urls in the file
    links = uniq(links) # eliminates duplicates
    links = filter(lambda x : os.path.isfile(WIKI_DIR + x), links) # get rid of bad paths
    links = map(lambda x : x.lower(), links) # lowercase everything
    
    return links

'''
eliminates duplicates from a list
'''
def uniq(old_list):
    new_list = []
    already_seen = sets.Set([])
    for x in old_list:
        if x in already_seen:
            continue
        else:
            new_list.append(x)
            already_seen.add(x)
    return new_list

'''
returns the path to get to s, with "parent" dictionary
(mapping each page to the one you come from to get to it
'''
def the_path(s, parent):
    road = [s]
    while parent[s] != None:
        road.append(parent[s])
        s = parent[s]
    road.reverse()
    return road

'''
Executes BFS. If there is a destination, it returns the path. Otherwise, 
it returns prev. If a prebuilt wiki_dict (a dictionary consisting as paths to
pages as keys, and the links on those pages as values), it uses it, otherwise it builds one. This is an optimization that speeds things up when you execute multiple BFSs on the same directory of articles.
'''
def BFS(src, dest = None, wiki_dict = None):
    global visited
    global prev

    src = src.lower() #makes lowercase
    
    if dest:
        dest = dest.lower() #makes lowercase

    if not wiki_dict:  #if just using bfs from command line
        wiki_dict = analytics.load_links()

    q = [src] # initialize our queue
    prev[src] = None # there is no previous page
    visited.add(src) 
    
    while len(q) > 0:
        #pop an element off the queue and mark it as visited
        s = q.pop(0)

        #return if it's what we're looking for and print the path
        if s == dest:
            return the_path(s, prev)
            #extract all the pages it links to
        links = wiki_dict[s]
        #set the parent, add all the links to the queue, and mark them as visited
        for p in links:
            if not p in visited:
                prev[p] = s
                q.append(p) 
                visited.add(p)
    r = prev
    visited = sets.Set() # reinitialize these globals
    prev = {}        
    return r
