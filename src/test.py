#!/usr/bin/env python

import analytics
import bfs

my_dict = analytics.load_links()
'''
for x in my_dict.keys():
	print x
'''


print analytics.most_links()
print analytics.center()

