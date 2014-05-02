#!/usr/bin/env python

import analytics
import bfs

wiki_dict = analytics.load_links()

print "The most popular article in Wikipedia is %s" % analytics.most_links(wiki_dict)
print "The center of Wikipedia is %s" analytics.center(wiki_dict)
