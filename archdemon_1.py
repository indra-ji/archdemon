""" Implentation of Shannon's Demon for one stock. """

#Module imports 
import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import time

""" No rebalancing."""


#50/50 split between stock and cash. 
#1000 coin flips. 
#Heads = Up 1% 
#Tails = Down 0.99...%

#Set starting variables
stock_no = 1
stock = 50. 
cash = 50. 
balance = stock / (stock+cash)
flips = 1000
heads_move = 1. + 0.01
tails_move = 1. / heads_move

#Prepare Pandas dataframe
demon = pd.DataFrame(columns=['Stock', 'Cash', 'Returns'])

for i in range(0, flips+1, 1):
    demon.loc[i] = [stock, cash, 0]

# Coin flip and fill up values
for i in range(1, flips+1, 1): 
    coin = rd.randint(0,1)
    if (coin == 0):
        demon.loc[i, 'Stock'] = demon.loc[i-1, 'Stock'] * heads_move
    elif (coin == 1):
        demon.loc[i, 'Stock'] = demon.loc[i-1, 'Stock'] * tails_move
    
    demon.loc[i, 'Returns'] = (demon.loc[i, 'Stock'] + demon.loc[i, 'Cash']) 

# PLot it as as a TimeSeries graph
plt.figure(figsize=(12,8))
plt.plot(demon['Returns'])
plt.title('Demon')
plt.xlabel('Flips')
plt.ylabel('Returns')
#plt.show()

print(demon)


""" Rebalancing."""
""""
#50/50 split between stock and cash. 
#1000 coin flips. 
#Heads = Up 1% 
#Tails = Down 0.99...%

#Set starting variables
stock_no = 1
stock = 50. 
cash = 50. 
balance = stock / (stock+cash) #Proportion of the stock relative to total 
flips = 1000
heads_move = 1. + 0.01
tails_move = 1. / heads_move

#Prepare Pandas dataframe
demon = pd.DataFrame(columns=['Stock', 'Cash', 'Returns'])

for i in range(0, flips+1, 1):
    demon.loc[i] = [stock, cash, 0]

# Coin flip and fill up values
for i in range(1, flips+1, 1): 
    coin = rd.randint(0,1)
    if (coin == 0):
        demon.loc[i, 'Stock'] = demon.loc[i-1, 'Stock'] * heads_move
    elif (coin == 1):
        demon.loc[i, 'Stock'] = demon.loc[i-1, 'Stock'] * tails_move
    
    combined = demon.loc[i, 'Stock'] + demon.loc[i, 'Cash'] 
    demon.loc[i, 'Stock'] = combined * balance
    demon.loc[i, 'Cash'] = combined * balance
    demon.loc[i, 'Returns'] = (demon.loc[i, 'Stock'] + demon.loc[i, 'Cash']) - (stock+cash)

# PLot it as as a TimeSeries graph
plt.figure(figsize=(12,8))
plt.plot(demon['Returns'])
plt.title('Demon')
plt.xlabel('Flips')
plt.ylabel('Returns')
#plt.show()

print(demon)

"""