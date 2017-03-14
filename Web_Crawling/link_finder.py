from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    def