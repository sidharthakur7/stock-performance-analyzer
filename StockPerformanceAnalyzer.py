#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

stock = yf.download("TCS.NS", start="2020-01-01", end="2026-03-14")
data.columns=data.columns.get_level_values(0)

data['Daily Return']=data['Close'].pct_change()

total_return=(data['Close'].iloc[-1]/data['Close'].iloc[0]-1)*100
mean_return=data['Daily Return'].mean()*100
volatility=data['Daily Return'].mean()*100
max_gain=data['Daily Return'].max()*100
max_loss=data['Daily Return'].max()*100

print("\n STOCK PERFORMANCE ANALYSIS \n")

print(f"Stock:{stock}")
print(f"Average Daily Return:{mean_return:.2f}%")
print(f"Volatility (Risk):{volatility:.2f}%")
print(f"Max Daily Gain: {max_gain:.2f}%")
print(f"Max Daily Loss: {max_loss:>2f}%")

#Insights

print("\n Insights:")
if volatility >2:
    print("High Risk Stock")
else:
    print("Relatively Stable Stock")

if total_return>0:
    print("Overall Positive Return")
else:
    print("Negative Return")






# In[ ]:




