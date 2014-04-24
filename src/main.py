#!/usr/bin/env python

import re
import os
import sets
import pprint

visited = sets.Set([])
prev = {}
WIKI_DIR = '/Users/kevinrankine/wikipedia-game/wiki/'

def extract_links(path):
    text = open(path).read() # open the file for reading
    
    pat = re.compile('<a href=[\'"]?([^\'" >]+)') # regexp for link urls
    links = re.findall(pat, text) # find the links urls in the file
    
    links = map(lambda x : WIKI_DIR + x, links) # prepend all these filenames with WIKI_DIR
    links = filter(lambda x : os.path.isfile(x), links) # get rid of false files
    links = filter(lambda x : not x in visited, links) # get rid of files already visited
    
    return links
    
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

def print_path(s):
    road = [s]
    while prev[s] != None:
        road.append(prev[s])
        s = prev[s]
    road = reverse(road)
    pprint.pprint(road)
        
def BFS(src, dest):
    src = WIKI_DIR + src
    dest = WIKI_DIR + dest
    q = [src]
    prev[src] = None
    global visited
    while len(q) > 0:
        #pop an element off the queue and mark it as visited
        s = q.pop(0)
        visited.add(s)
        
        #return it if it's what we're looking for
        if os.path.abspath(s) == os.path.abspath(dest):
            print_path(s)
            return s
            #extract all the pages it links to
        links = extract_links(s)
        #set the previous
        for p in links:
            prev[p] = s
            q = q + links
        q = uniq(q)
