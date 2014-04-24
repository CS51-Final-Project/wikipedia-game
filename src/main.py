#!/usr/bin/env python

import re
import os
import sets

visited = sets.Set([])
prev = {}
WIKI_DIR = '/Users/kevinrankine/wikipedia-game/wiki/'

def extract_links(path):
    text = open(path).read() # open the file for reading
    
    pat = re.compile('<a href=[\'"]?([^\'" >]+)') # regexp for link urls
    links = re.findall(pat, text) # find the links urls in the file
    
    links = map(lambda x : WIKI_DIR + x, links) # prepend all these filenames with WIKI_DIR
    links = filter(lambda x : os.path.isfile(x), links) # get rid of bad paths
    links = filter(lambda x : not x in visited, links) # get rid of files already visited
    links = uniq(links)

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
    road.reverse()
    for p in road:
        print p
        
def BFS(src, dest):
    src = WIKI_DIR + src
    dest = WIKI_DIR + dest
    q = [src]

    global visited
    global prev

    visited = sets.Set()
    prev = {}
    prev[src] = None    
    
    while len(q) > 0:
        print map(lambda x : x.split("/")[-1], q), "\n"
        #pop an element off the queue and mark it as visited
        s = q.pop(0)
        if s in visited:
            continue
        else:
            visited.add(s)
            #return if it's what we're looking for
            if os.path.abspath(s) == os.path.abspath(dest):
                print_path(s)
                return
                #extract all the pages it links to
            links = extract_links(s)
                #set the previous
            for p in links:
                prev[p] = s
                q.append(p)
            
