import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('http://www.tamilanguide.in/2015/12/tamilnadu-govt-jobs-2016-17117-vacancies.html').read()

soup = bs.BeautifulSoup(sauce,'html.parser')
#print(soup.prettify())
#print(soup.p)

#for paragraph in soup.find_all('a'):
   # print(paragraph.string)
    
#for url in soup.find_all('a'):
    #print(url.get('href'))

#last_link = soup.find("div", id="categorySidebar")
#flink = first_link.find_all_previous("p")


print(soup.p)
