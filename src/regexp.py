import re
f = open('index.html')
text = f.read()
pat = re.compile('href=[\'"]?([^\'" >]+)')
links = re.findall(pat, text)

print links
