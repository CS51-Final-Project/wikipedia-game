#!/usr/bin/env python

import main
import os

src = "../wiki/Nickelodeon_(TV_channel)"
dest = "../wiki/New_York_City"

print main.BFS(src, dest)
print main.print_path(os.path.abspath(dest))
#print main.extract_links(src)
