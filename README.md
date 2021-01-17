# Monte-Carlo-Stock-Simulation
This is a program that takes in historical prices for a stock ticker (in my example TSLA) and uses this data along with statistics and probability theory to predict the price of the ticker after a configurable number of days. This project was written on Spyder and used the following libraries: numpy, pandas, pandas_datareader, matplotlib, scipy, datetime, and time.

# Motivation
I made this project for a math essay I wrote in grade 12 as a requirement for completing the IB Diploma Programme. The essay itself is also included in this repository to provide more explanation on the math included in the formulas, as well as the sources I used to gather my research.

# How to use?
The first component of the code is used to set the stock ticker and set the timeframe for gathering prices.

![Data](https://github.com/DavidLoi/Monte-Carlo-Stock-Simulation/blob/main/Screenshots/Data.PNG)

In this example, I've used the ticker symbol TSLA, and I gathered the closing prices from June 28th, 2010 all the way until December 31st, 2019. All of this can be changed to suit any needs.

This is where the duration of the simulation, and the number of simulations is set.

![Simulation Settings](https://github.com/DavidLoi/Monte-Carlo-Stock-Simulation/blob/main/Screenshots/SimulationSettings.PNG)

I predicted prices 23 days into the future for a total of 10000 simulations.

Finally, after the code has finished executing, it will produce 4 figures and some other statistics and information.

The stock chart from the "start" date till the "end" date.

![Stock Chart](https://github.com/DavidLoi/Monte-Carlo-Stock-Simulation/blob/main/Screenshots/StockChart.png)

The log returns for each day from the "start" date till the "end" date.

![Log Returns](https://github.com/DavidLoi/Monte-Carlo-Stock-Simulation/blob/main/Screenshots/LogReturns.png)

The movement of the stock's price over the configurable number of days into the future for each simulation.

![Simulation](https://github.com/DavidLoi/Monte-Carlo-Stock-Simulation/blob/main/Screenshots/Simulation.png)

A frequency chart which takes the last day of each simulation and displays how often each price occured, the blue line represents the price of the stock on the ending date.

![Frequency Chart](https://github.com/DavidLoi/Monte-Carlo-Stock-Simulation/blob/main/Screenshots/FrequencyChart.png)

**Note: The simulation result and frequency chart posted here are different than those from the essay due to the random aspect of the simulation making it practically impossible to reproduce the same results.

Basic stastical figures printed in the console.

![Stats](https://github.com/DavidLoi/Monte-Carlo-Stock-Simulation/blob/main/Screenshots/Stats.PNG)

A markov chain highlighting the probability of the price going up or down depending on what happened the previous day.

![Markov Chain](https://github.com/DavidLoi/Monte-Carlo-Stock-Simulation/blob/main/Screenshots/MarkovChain.PNG)

The total time the code took to execute.

![Time](https://github.com/DavidLoi/Monte-Carlo-Stock-Simulation/blob/main/Screenshots/Time.PNG)

**Note: Context and explanations for the formulas and math process are available in the essay.
