import bs4 as bs
import urllib.request
import requests

import re
import json
import csv
import io
#import pandas as pd


   

#with open("jobdata.csv",'wb')as f:
    #writer = csv.writer(f)
   

#f = open(filename, "w")
#headers = "Tamilnadu Job\n"
#f.write(headers)

sauce = urllib.request.urlopen('http://www.tngovernmentjobs.in/').read()

soup = bs.BeautifulSoup(sauce,'html.parser')

g_data = soup.find_all("div", {"class":"widget Blog"})



#===========titleonly==================

titleonly= soup.find_all('h2', {"class":"post-title entry-title"})

for titleall in titleonly:
    title = titleall.text

titleonly= soup.find_all('h2', {"class":"post-title entry-title"})
title = titleonly[0].text.strip()
#title = titleonly[0].text

print(title)
#===========contentonly==================
content_text = soup.find_all(class_="post-body entry-content")

#for contentonly in content_text:
    #content = contentonly.text
content_text = soup.find_all(class_="post-body entry-content")
content = content_text[0].text.strip()

    
    #print(contentonly.text)
#===========imgonly==================
img2 = soup.find_all('div',{"class":"post-body entry-content"})

#img1 = soup.find(id="summary410844854653072811").find('img')

#for div in img2:
    #imgjob = div.img.get('src')

img1 = soup.find(id="summary410844854653072811").find('img')

    #print(div.img.get('src'))
#===========img only End==================

dict = {}
dict['title'] = title
dict['discription'] = content
#dict['img'] = imgjob
#print ('\result:{}'.format(dict))

filename = "D://tnjob.csv"
f= open(filename, "w")
f_out=open("filename, "w"")
headers = "title,content,img\n"
f.write(headers)
for line in f:
    tokens=line.split('')
    f_out.write("count" +str(len(tokens))+line)
f.write("title\n",title)
#f.write(content)
#f.write(imgjob)
print("writing complete")
f.close()
f_out.close()


#=================================
