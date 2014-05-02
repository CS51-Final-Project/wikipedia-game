#!/usr/bin/env python

import analytics
import bfs

wiki_dict = analytics.load_links()

print "The most popular article in Wikipedia is %s" % analytics.most_links(wiki_dict)
print "The center of Wikipedia is %s" analytics.center(wiki_dict)

print "ARTICLE occurs %s number of times" % analytics.link_frequency(ARTICLE, wiki_dict)
print "ARTICLE is referenced on these pages: \n %s" % analytics.where_referenced(ARTICLE, wiki_dict)
