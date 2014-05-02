#!/usr/bin/env python
import sys
import analytics
import bfs

wiki_dict = analytics.load_links()

print "The most popular article in Wikipedia is {0}".format(analytics.most_links(wiki_dict))
print "The center of Wikipedia is {0}".format(analytics.center(wiki_dict))

print "The shortest path between {0} and {1} is following the following links: \n {2}".format(argv[1], argv[2], (bfs.BFS(argv[1], argv[2], wiki_dict)))
analytics.link_frequency(argv[1], wiki_dict)
analytics.where_referenced(argv[1], wiki_dict)
