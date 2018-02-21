import bs4 as bs
#import BeautifulSoup
import urllib.request
#import request, urlopen
import re

import json


sauce = urllib.request.urlopen('http://www.tngovernmentjobs.in/').read()

soup = bs.BeautifulSoup(sauce,'html.parser')


name_Title = soup.find('h2', attrs={'class': 'post-title entry-title'})
name = name_Title.text.strip()
#print (name)



cont1 = soup.find(id="summary410844854653072811")
content_Name = cont1.text.strip()
#print(content_Name)

img1 = soup.find(id="summary410844854653072811").find('img')
#print(img1)

#==========================================================================
links = soup.find_all('a')
#for link in links:
  #print(link)

data= soup.find_all('h2', {"class":"post-title entry-title"})

for item in data:
      print(item.text)
      print(item.contents[0])
    

names = item.contents[0]
print(names)


    

cont1 = soup.find(id="summary410844854653072811")
content_Name = cont1.text.strip()
print(content_Name)

img1 = soup.find(id="summary410844854653072811").find('img')
print(img1)


#data_content= soup.find_all('div', {"class":"post-body entry-content"})

#for item_content in data_content:   
     #  print(item_content.text)
      

#data_img = soup.find_all('span', {"itemp":"btnt-img"})

#for item_content in data_img:   
      #print(item_content)


