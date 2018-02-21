import bs4 as bs
import urllib.request
import requests

import re
import json
#import pandas as pd


sauce = urllib.request.urlopen('http://www.tngovernmentjobs.in/').read()

soup = bs.BeautifulSoup(sauce,'html.parser')

g_data = soup.find_all("div", {"class":"widget Blog"})

#===========titleonly==================

titleonly= soup.find_all('h2', {"class":"post-title entry-title"})

for title in titleonly:    

    print(title.text)
#===========contentonly==================
content_text = soup.find_all(class_="post-body entry-content")

for contentonly in content_text:
    
    print(contentonly.text)
#===========imgonly==================
img2 = soup.find_all('div',{"class":"post-body entry-content"})

#img1 = soup.find(id="summary410844854653072811").find('img')

for div in img2:

    print(div.img.get('src'))
#===========img only End==================

dict = {}
dict['title'] = title.text
dict['discription'] = contentonly.text
dict['img'] = div.img.get('src')
print ('\result:{}'.format(dict))
