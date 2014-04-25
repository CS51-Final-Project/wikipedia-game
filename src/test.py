#!/usr/bin/env python

import analytics
import bfs

wiki_dict = analytics.load_links()

analytics.most_links(wiki_dict)
