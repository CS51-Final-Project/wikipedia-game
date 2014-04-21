#!/usr/bin/env python

import main

src = "a.html"
dest = "c.html"

print main.BFS(src, dest)
main.print_path(dest)
#print main.extract_links(src)
