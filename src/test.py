#!/usr/bin/env python

import analytics
import bfs

my_dict = analytics.load_links()

for keys, values in my_dict:
	print(keys)
	print(values)