from bs4 import BeautifulSoup
from urllib.request import urlopen
r = urlopen('http://www.google.com')
soup = BeautifulSoup(r)
print (type(soup))