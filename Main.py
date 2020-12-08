"""Clustering Algorithm"""



"""1-D"""

import numpy as np
import matplotlib.pyplot as plt
import random



def data_list(n, max):
    list = []
    for i in range(n):
        list.append(random.randint(0,max))
    list.sort()
    return list
        

ar = data_list(5,10)
val = 0

def plot_at_y(arr, val,c='g',m='o', **kwargs):
    plt.plot(arr, np.zeros_like(arr) + val, 'x',color=c, marker=m, **kwargs) #np.zero_like(arr) creates a list of zeros
    plt.show()

plot_at_y(ar,val)


#This alrorithm finds the difference from point i with all other points  
def cluster_alg(list,k):
    list_of_indexes = []
    dict = {}
    
    counter = 0
    counter_2 = 0
    
    for i in range(len(list)):
        list_of_indexes.append(i)
    
    list_of_choices =  random.sample(list_of_indexes,k)
        
    for i in list_of_choices:
        for k in list:
            #if i != list.index(k):
            counter = counter +abs(list[i]-k)
            dict[list_of_choices.index(i)]=counter
    print(list_of_choices)
    
    for i in range(len(dict)-1):
    
        dict[i] = dict[i]-counter_2
        counter_2 = counter_2 +dict[i]
    
    dict[len(list_of_choices)-1] = dict[len(list_of_choices)-1] - counter_2   
    
    
            
        
                
    return dict

print(cluster_alg(ar,3))
print(ar)
    
    