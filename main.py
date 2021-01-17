# Libraries
import numpy as np  
import pandas as pd  
from pandas_datareader import data as wb  
import matplotlib.pyplot as plt  
from scipy.stats import norm
import datetime as dt
import time

#Timer
start_time = time.time()

# Data
stock = "TSLA"
data = pd.DataFrame()
start = dt.datetime(2010, 6, 28)
end = dt.datetime(2019, 12, 31)
data[stock] = wb.DataReader(stock, 'yahoo', start, end)['Adj Close']

# Log Returns
log_returns = np.log(1 + data.pct_change())

# Test
data.plot(figsize=(10, 6));
log_returns.plot(figsize = (10, 6))

# Mean
u = log_returns.mean()

# Variance
var = log_returns.var()

# Drift
drift = u - (0.5 * var)

# Standard Deviation
stdev = log_returns.std()

# Brownian Motion
days = 23
sims = 10000

z = norm.ppf(np.random.rand(days, sims))

daily_returns = np.exp(np.array(drift) + np.array(stdev) * z)

# Expected Returns
s0 = data.iloc[-1]
price_list = np.zeros_like(daily_returns)
price_list[0] = s0

for t in range(1, days):
    price_list[t] = price_list[t-1] * daily_returns[t]
    
plt.figure(figsize=(10,6))
plt.plot(price_list)
plt.show()

results = price_list[-1]

results.sort()
min = int(np.floor(results[0]))
max = int(np.ceil(results[-1]))

#Statistics
print()
print("Mean: " + str(np.mean(results)))
print("SD: " + str(np.std(results)))
print("Max: " + str(np.max(results)))
print("Min: " + str(np.min(results)))
print("5%: " + str(np.percentile(results, 5)))
print("25%: " + str(np.percentile(results, 25)))
print("75%: " + str(np.percentile(results, 75)))
print("95%: " + str(np.percentile(results, 95)))
print()


#Frequency
freq = [0 for i in range(max - min + 1)]
for i in results:
    freq[int(np.round(i)) - min] += 1
    
new_prices = np.arange(min, max + 1, 1)

plt.bar(new_prices, freq)
plt.xlabel('Prices', fontsize = 12)
plt.ylabel('Frequency', fontsize = 12)
plt.axvline(x = data[stock][-1], color = 'b', linestyle = '-')
plt.title('Monte Carlo Simulation Distribution: TSLA')
plt.show()

#Constructing Markov Chain
p = 0
n = 0
pp = 0
pn = 0
np = 0
nn = 0

for day in range(days-1):
    for sim in range(sims):
        if daily_returns[day][sim] > 1:
            p += 1
            
            if daily_returns[day+1][sim] > 1:
                pp += 1
            else:
                pn += 1
                
        elif daily_returns[day][sim] < 1:
            n += 1
            
            if daily_returns[day+1][sim] > 1:
                np += 1
            else:
                nn += 1

#Results
print("Previous price movement was positive:")
print("Probability of moving up: " + str(pp/p))
print("Probability of moving down: " + str(pn/p))
print()
print("Previous price movement was negative:")
print("Probability of moving up: " + str(np/n))
print("Probability of moving down: " + str(nn/n))
print()

#End Timer
end_time = time.time()

print("Time elapsed: " + str(end_time-start_time))

print()