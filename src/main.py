#!/usr/bin/env python

import re

marked = {}
previous = {}

def extract_links(path):
    f = open(path)
    text = f.read()
    pat = re.compile('href=[\'"]?([^\'" >]+)')
    links = re.findall(pat, text)
    return links

def visited(path): 
    try:
        return marked[path]
    except(Exception):
        return False

def print_path(s, hist):
    road = []
    while prev[s] != None:
        road.append(prev[s])
        s = prev[s]
        
        
def BFS(src, dest):
    q = [src]
    prev[src] = None
    while len(q) > 0:
        #pop an element off the queue
        s = q[0]
        #return it if it's what we're looking for
        if s == dest:
            return s
        #extract all the pages it links for
        links = filter(visited, extract_links(s))
        #set the previous
        for p in links:
            previous[p] = s
        q.append(links)
        
        
