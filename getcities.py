import requests
from bs4 import BeautifulSoup
import os
import re

res=requests.get("https://www.groupon.com/local")
soup=BeautifulSoup(res.content, 'lxml')

section=soup.find('ul', attrs={'class': 'unstyled block-grid four-up'})

links=section.find_all('a', href=re.compile("/local/"))

urls=[]
for link in links:
    urls.append("https://www.groupon.com"+link.get('href')+"/cities")    

with open("states.txt","a") as file:
    for url in urls:
        file.write(url+'\n')

def getcities(url):
    res=requests.get(url)
    soup=BeautifulSoup(res.content, 'lxml')
    try:
        links=soup.find('ul', attrs={'class': 'unstyled block-grid five-up'}).find_all('a', href=re.compile("https://www.groupon.com/local/"))
    except:
        print(url)
        pass
    city_urls=[]
    cities=[]
    state=url.replace('https://www.groupon.com/local/','').replace('/','').replace('cities', '_cities')
    with open(state+"_link.txt","a") as file:
        for link in links:
            city_urls.append(link.get('href'))
            file.write(link.get('href')+'\n')
    with open(state+"_name.txt","a") as file:
        for link in links:
            cities.append(link.text)
            file.write(link.text+'\n')
   
for url in urls:
    getcities(url)

