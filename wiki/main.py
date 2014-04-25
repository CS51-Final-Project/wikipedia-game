#!/usr/bin/env python

import re
import os

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

def print_path(s):
    road = [s]
    while prev[s] != None:
        road.append(prev[s])
        s = prev[s]
    print road
        
        
def BFS(src, dest):
    q = [src]
    prev[os.path.abspath(src)] = None
    global marked
    while len(q) > 0:
        #pop an element off the queue
        s = q.pop(0)
        marked[s] = True
        #return it if it's what we're looking for
        if os.path.abspath(s) == os.path.abspath(dest):
            return s
            
        #extract all the pages it links for, filter for not visited
        links = filter(lambda x : not visited(x), extract_links(s))
        
        #set the previous
        for p in links:
            prev[os.path.abspath(p)] = os.path.abspath(s)
        q = q + links