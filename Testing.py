# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 22:24:05 2020

@author: peter
"""
import random

list = [4,2,6,8,4]
list_1 = [0,1,2]
counter = 0
dict = {}
for i in list_1:
    for k in list:
        if i != list.index(k):
            counter= counter +abs(list[i]-k)
            dict[i]=counter

counter = 0            
for i in range(len(dict)-1):
    
    dict[i] = dict[i]-counter
    counter = counter +dict[i]
    
dict[len(list_1)-1] = dict[len(list_1)-1] - counter    
print (dict)
print(counter)  


"""            
list = [1,2,3,4,5]

UpdatedList = random.sample(list, 5)
print(UpdatedList)

print(type(UpdatedList))
"""        