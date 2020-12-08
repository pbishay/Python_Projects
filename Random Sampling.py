# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:52:39 2020

@author: peter
"""
import numpy as np
import matplotlib.pyplot as plt

def histogram_plot(data, bins, plot_title):  
    plt.title(plot_title)
    plt.xlabel('Observations')
    plt.ylabel('Count')
    plt.hist(data, bins)   
    plt.show()
    
# Test Function

#np.random.seed(4288)    
random_data = np.random.choice(range(11), 100)
bins = int(100**.334 * 2)
histogram_plot(random_data, bins, 'Sample Histogram')

def sample(number_of_samples, sample_size=50, dist='uniform'):
    data = []
    for k in range(number_of_samples):
        if dist == 'uniform':
            random_data = np.random.exponential(.5, size=sample_size)
            
            data.append(np.mean(random_data))
    return data
        
sample_sizes = [10, 100, 1000, 10000, 100000, 1000000]
for n in sample_sizes:
    sample_means = sample(n)
    histogram_plot(sample_means, int(n**.334 * 2), f'sample size = {n}')
    