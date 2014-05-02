#!/usr/bin/env python
import sys
import analytics
import bfs

#loads a compressed dictionary to be used in all functions
wiki_dict = analytics.load_links()

#runs BFS on the two articles
shortest_path = bfs.BFS((sys.argv[1]).lower(), (sys.argv[2]).lower(), wiki_dict)

#if the destination article is a few pages away, returns the path
#else says article is on page
if type(shortest_path) == dict:
	print "The two articles are in no way connected"
elif len(shortest_path) > 2:
	print "The shortest path between {0} and {1} is following the following links: \n {2}".format((sys.argv[1]).lower(), (sys.argv[2]).lower(), shortest_path)
else:
	print "{0} is a direct link from {1}".format(sys.argv[2], sys.argv[1])

#if user wants analytics and provides "-analytics" then runs
if len(sys.argv) == 4 and sys.argv[3] == "-analytics":
	print "\n"
	#checks references for the starting article
	raw_input("List pages that reference {0}? ".format(sys.argv[1]))
	analytics.where_referenced((sys.argv[1]).lower(), wiki_dict)

	#checks references for the destination article
	raw_input("List pages that reference {0}? ".format(sys.argv[2]))
	analytics.where_referenced((sys.argv[2]).lower(), wiki_dict)

	#finds the most popular page on wikipedia
	raw_input("Find the most popular page on Wikipedia? ")
	print "The most popular three articles in Wikipedia are: \n{0}".format(analytics.most_links(wiki_dict))
	print "\n"

	#finds the center of wikipedia
	raw_input("Continue? ")
	print "Initializing Microprocessors..."
	raw_input("Start Search for Center? ")
	print "The center of Wikipedia is {0}".format(analytics.center(wiki_dict))
	print "\n"


