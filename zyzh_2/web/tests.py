from django.test import TestCase

# Create your tests here.

from bs4 import BeautifulSoup

from pymongo import MongoClient

# conn = MongoClient('192.168.0.0.1', 27017)
# db = conn.mydb
# my_set = db.test_set


# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
#
# soup=BeautifulSoup(html,'lxml')
# print soup.p.attrs
# print soup.find_all("p")
tuple = (x for x in range(4))
list=[x for x in range(4)]

