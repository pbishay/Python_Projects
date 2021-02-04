# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 21:02:24 2021

@author: peter
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


head={'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}

dict = {}

for i in range(1,126):
        dict[i]=[]

list = []
 
for i in range (1,126):
    results=requests.get("https://swingtradebot.com/equities?page="+str(i),headers=head)
    src=results.content
    soup = BeautifulSoup(src, 'lxml')
    tab = soup.find("table",{"class":"table table-striped table-bordered"})
    x=tab.find_all('a', href=True)
    
    for j in x:
        if "/equities/" in  j['href']: 
            dict[i].append(j['href'])
    for a in dict[i]:
        newstr=a.replace("/equities/", "")
        list.append(newstr)
  
del list[1::2]
    
    
print(list)
print(len(list))
    


