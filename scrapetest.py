import requests
from bs4 import BeautifulSoup

################################################################ Parsing a Page 
"""
ugm = "https://www.ugm.ac.id/id/post/viewrilisall"
ugm1 = requests.get(ugm)
berita = BeautifulSoup(ugm1.content, "html.parser")
ptitles = berita.find_all("div", class_ = "post-title")
lizt = []
for _ in ptitles:
    date = _.find("span", class_ = "post-date").string
    title = _.select("a[title]")[0].string.strip()
    lizt.append((title , date))
print(lizt)
"""
################################################################### Parsing several Pages
"""
ugm = "https://www.ugm.ac.id/id/post/viewrilisall?page=%i"
lizt = []
for _ in range(1,10):
    urlgm = requests.get(ugm%_)
    berita = BeautifulSoup(urlgm.content, "html.parser")
    ptitles = berita.find_all("div", class_ = "post-title")
    for _k in ptitles:
        date = _k.find("span", class_ = "post-date").string
        title = _k.select("a[title]")[0].string.strip()
        lizt.append((title , date))
print(lizt)
"""
##################################################################### Parsing some unavailable pages
s = [1,2,3,4,5,6,7,8,9,10,1500,1501, 1502, 4]
ugm = "https://www.ugm.ac.id/id/post/viewrilisall?page=%i"
lizt = []
for _ in s:
    urlgm = requests.get(ugm%_)
    berita = BeautifulSoup(urlgm.content, "html.parser")
    ptitles = berita.find_all("div", class_ = "post-title")
    if len(ptitles) == 0 : break
    else:
        for _k in ptitles:
            date = _k.find("span", class_ = "post-date").string
            title = _k.select("a[title]")[0].string.strip()
            lizt.append((title , date))
    
print(lizt)