#!/usr/bin/env python

import re

marked = {}
prev = {}

def extract_links(path):
    try:
        f = open(path)
        text = f.read()
        pat = re.compile('<a href=[\'"]?([^\'" >]+)')
        links = re.findall(pat, text)
        return links
    except(Exception):
        return []

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
    global marked
    while len(q) > 0:
        #pop an element off the queue
        s = q.pop(0)
        marked[s] = True
        print s
        
        #return it if it's what we're looking for
        if s == dest:
            return s
            
        #extract all the pages it links for, filter for not visited
        links = filter(lambda x : not visited(x), extract_links(s))
        
        #set the previous
        for p in links:
            prev[p] = s
        q = links + q
        
        
