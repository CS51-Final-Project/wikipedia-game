#!/usr/bin/env python

import re
import main

#dictionary for links
popular = {}

global marked


def load_dict(path):
	f = open(path)
	text = f.read
	pat = re.compile('<a href=[\'"]?([^\'" >]+)')
    links = re.findall(pat, text)
    while len(links) > 0:
    	if links[0] in dict.keys():
    		popular[links[0]] += 1; #update frequency of link
    	else:
    		popular[links.pop(0)] = 1; #add element to dictionary
    for x in links:
    	load_dict(x)

