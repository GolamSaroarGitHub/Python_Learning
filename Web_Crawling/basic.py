import urllib
from urllib.request import urlopen
thisurl = "http://www-rohan.sdsu.edu/~gawron/index.html"

handle = urlopen(thisurl)

html_gunk =  handle.read()

print(html_gunk)