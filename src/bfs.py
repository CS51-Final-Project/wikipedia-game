#!/usr/bin/env python

import re
import os
import sets
import analytics

visited = sets.Set([])
prev = {}
WIKI_DIR = os.path.abspath("../wiki") +"/"

def extract_links(path):
    text = open(path).read() # open the file for reading
    pat = re.compile('<a href=[\'"]?([^\'" >]+)') # regexp for link urls
    
    links = re.findall(pat, text) # find the links urls in the file
    links = uniq(links)
    # links = map(lambda x : WIKI_DIR + x, links) # prepend all these filenames with WIKI_DIR
    links = filter(lambda x : os.path.isfile(WIKI_DIR + x), links) # get rid of bad paths
    links = filter(lambda x : not x in visited, links) # get rid of files already visited
    links = map(lambda x : x.lower(), links)
    
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

def print_path(s, parent):
    road = [s]
    while s in parent[s] != None:
        road.append(parent[s])
        s = parent[s]
    road.reverse()
    for p in road:
        print p
def BFS(src, dest = None, wiki_dict = None):
    global visited
    global prev

    all_links = analytics.load_links()
    src = src.lower()
    
    if dest:
        dest = dest.lower()
    q = [src]
    visited.add(src)
    prev[src] = None    
    
    while len(q) > 0:
        #pop an element off the queue and mark it as visited
        s = q.pop(0)
        if s in visited:
            continue
        #return if it's what we're looking for and print the path
        if dest and os.path.abspath(s) == os.path.abspath(dest):
            print_path(dest, prev)
            return prev
            #extract all the pages it links to
        if wiki_dict:
            links = wiki_dict[s]
        else:
            links = extract_links(s)
        #set the parent, add all the links to the queue, and mark them as visited
        for p in links:
            prev[p] = s
            q.append(p)
            visited.add(p)
    r = prev
    visited = sets.Set()
    prev = {}            
    print "did it"
    return r
