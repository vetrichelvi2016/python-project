import bs4 as bs
import urllib.request
import requests

import re
import json
#import pandas as pd


sauce = urllib.request.urlopen('http://www.tngovernmentjobs.in/').read()

soup = bs.BeautifulSoup(sauce,'html.parser')

g_data = soup.find_all("div", {"class":"widget Blog"})

titleonly= soup.find_all('h2', {"class":"post-title entry-title"})
only_title = titleonly.text.strip()
print(only_title)

fdiv = soup.find(class_="widget Blog").get_text()
#print(fdiv)
title_text = soup.find_all(class_="post-title entry-title")
title = title_text[0]
#print(title_text)

content_text = soup.find_all(class_="post-body entry-content")
content = content_text[0]

img1 = soup.find(id="summary410844854653072811").find('img')
#print(title.text)
#print(content.text)
#print(img1)

dict = {}
dict['title'] = title.text
dict['discription'] = content.text
dict['img'] = img1
print ('\result:{}'.format(dict))

#===========================================================

   




