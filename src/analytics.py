#!/usr/bin/env python

import re
import main

#dictionary for links
popular = {}
visited = {}

global marked

#only gets all links from one path, not sure how to traverse directory and run on each file
def load_dict(path):
	links_not_to_visit_again = links_to_follow = links = extract_links(path)
	while len(links_not_to_visit_again) > 0:
		visited[links_not_to_visit_again.pop(0)] = 1;
    while len(links) > 0:
    	if links[0] in dict.keys():
    		popular[links[0]] += 1; #update frequency of link
    	else:
    		popular[links.pop(0)] = 1; #add element to dictionary
    for x in links_to_follow:
    	if x in visited.keys():
    		pass
    	else:
    	load_dict(x)

#returns key from dictionary with the most links
def most_links():
	return (sorted(popular, key=popular.__getitem__, reverse=True))[0]

def link_frequency(link):
	

