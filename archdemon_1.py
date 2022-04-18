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
flips = 1000000
heads_move = 1. + 0.5
tails_move = 1. / heads_move

#Prepare Pandas dataframe
demon_no_rb = pd.DataFrame(columns=['Stock', 'Cash', 'Total'])

for i in range(0, flips+1, 1):
    demon_no_rb.loc[i] = [stock, cash, 0]

# Coin flip and fill up values
for i in range(1, flips+1, 1): 
    coin = rd.randint(0,1)
    if (coin == 0):
        demon_no_rb.loc[i, 'Stock'] = demon_no_rb.loc[i-1, 'Stock'] * heads_move
    elif (coin == 1):
        demon_no_rb.loc[i, 'Stock'] = demon_no_rb.loc[i-1, 'Stock'] * tails_move
    
    demon_no_rb.loc[i, 'Total'] = (demon_no_rb.loc[i, 'Stock'] + demon_no_rb.loc[i, 'Cash']) 

# PLot it as as a TimeSeries graph
plt.figure(figsize=(12,8))
plt.plot(demon_no_rb['Total'])
plt.title('No Demon')
plt.xlabel('Flips')
plt.ylabel('Total')
plt.show()

""" Rebalancing."""

#50/50 split between stock and cash. 
#1000 coin flips. 
#Heads = Up 1% 
#Tails = Down 0.99...%

#Prepare Pandas dataframe
demon_rb = pd.DataFrame(columns=['Stock', 'Cash', 'Total'])

for i in range(0, flips+1, 1):
    demon_rb.loc[i] = [stock, cash, 0]

# Coin flip and fill up values
for i in range(1, flips+1, 1): 
    coin = rd.randint(0,1)
    if (coin == 0):
        demon_rb.loc[i, 'Stock'] = demon_rb.loc[i-1, 'Stock'] * heads_move
    elif (coin == 1):
        demon_rb.loc[i, 'Stock'] = demon_rb.loc[i-1, 'Stock'] * tails_move
    
    combined = demon_rb.loc[i, 'Stock'] + demon_rb.loc[i, 'Cash'] 
    demon_rb.loc[i, 'Stock'] = combined * balance
    demon_rb.loc[i, 'Cash'] = combined * balance
    demon_rb.loc[i, 'Total'] = (demon_rb.loc[i, 'Stock'] + demon_rb.loc[i, 'Cash']) 

# PLot it as as a TimeSeries graph
plt.figure(figsize=(12,8))
plt.plot(demon_rb['Total'])
plt.title('Demon')
plt.xlabel('Flips')
plt.ylabel('Total')
plt.show()

print(demon_rb)
