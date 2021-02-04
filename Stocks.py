# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 14:34:00 2020

@author: peter
"""
#Program determines when to purchase and sell stocks using duel moving average crossover

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
import yfinance as yf
import plotly.graph_objs as go

#Extract data from yahoo finance for desired stock, period, and interval 
Stock='AHCO'
Stock_data = yf.download(tickers=Stock, period='1d', interval='1m')
plt.style.use('ggplot')




#Create simple moving averages 

def ST_moving_average(data,amt=30):
    SMA30=pd.DataFrame()
    SMA30["Adj Close"]=data["Adj Close"].rolling(amt).mean()
    return SMA30
    
def LT_moving_average(data, amt=100):
    SMA100=pd.DataFrame()
    SMA100["Adj Close"]=data["Adj Close"].rolling(amt).mean()
    return SMA100





def total_data(data):
    t_data=pd.DataFrame()
    t_data["Adj Close"]=data["Adj Close"]
    t_data["SMA30"]=ST_moving_average(data)["Adj Close"]
    t_data["SMA100"]=LT_moving_average(data)["Adj Close"]
    return t_data


    
def buy_sell(data):
    sigPriceBuy = []
    sigPriceSell = []
    flag=-1
    
    for i in range (len(data)):
        if data["SMA30"][i]>data["SMA100"][i]:
            if flag != 1:
                sigPriceBuy.append(data["Adj Close"][i])
                sigPriceSell.append (np.nan)
                flag =1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        elif data["SMA30"][i] < data["SMA100"][i]:
            if flag !=0 and flag !=-1 :
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(data["Adj Close"][i])
                flag=0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)
    return (sigPriceBuy, sigPriceSell)

def buy_sell_data(data):
    data["Buy_Signal_Price"]=buy_sell(data)[0]
    data["Sell_Signal_Price"]=buy_sell(data)[1]
    
    return data
    

x=total_data(Stock_data)

x["Buy_Signal_Price"]=buy_sell(x)[0]
x["Sell_Signal_Price"]=buy_sell(x)[1]

print(x)

def data_history(data,alpha_):
    plt.figure(figsize=(12.5,4.5))
    plt.plot(data["Adj Close"],label=Stock, alpha=alpha_, color="green")
    plt.plot(data["SMA30"],label="SMA30",alpha=alpha_, color="blue")
    plt.plot(data["SMA100"],label="SMA100",alpha=alpha_, color="red")
    plt.plot(data["Buy_Signal_Price"],label="Buy",marker="^", color="green")
    plt.plot(data["Sell_Signal_Price"],label="Sell", marker="v", color="red")
    plt.title(f'{Stock} Adj. Closing Price History')
    plt.xlabel(f"{data.index[0]}             -                 {data.index[-1]}")
    plt.ylabel("Adj. Close Price USD ($)")
    plt.legend(loc="lower left")
    plt.show()

data_history(x, .5)

def profit(data,purchase):
    profit=0
    counter=0
    for i in range(len(data)):
        if data["Buy_Signal_Price"][i] >0:
            profit = profit -data["Buy_Signal_Price"][i]*purchase
            counter = counter +1
        if data["Sell_Signal_Price"][i] >0:
            profit = profit +data["Sell_Signal_Price"][i]*purchase
            counter = counter+1
        else:
            pass
    if (counter % 2) == 1:
        profit = profit+data["Adj Close"][-1]*purchase
    else:
        pass
        
    return profit
        
print(f"Profit: ${profit(x,1)}")
"""
for i in range(len(x)):
    print(x["Buy_Signal_Price"][i])
print("___________________________________________________________________")
    
for i in range(len(x)):
    print(x["Sell_Signal_Price"][i])
"""           
         
        

    





