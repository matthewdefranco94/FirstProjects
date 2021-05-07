import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pandas_datareader import data as web



##############
#Some user input here#





assets = ['FB' , 'TWTR' , 'CX' , 'NFLX' , 'AMD']

weightings = np.array([0.2 , 0.2 , 0.2 , 0.2 , 0.2])

stockStartDate = '2015-01-01'

today = datetime.today().strftime('%Y-%m-%d')

df = pd.DataFrame()

for stock in assets:
    df[stock] = web.DataReader(stock , data_source = 'yahoo' , start = stockStartDate , end = today)['Adj Close']


title = 'Portfolio adj price history'

my_stocks = df


def returns():
#create and plot graph (loops through each column)
    for columns in my_stocks.columns.values:
        my_stocks[columns] = my_stocks[columns].pct_change(periods = 1)
        plt.plot(my_stocks[columns] , label = my_stocks)

    plt.title(title)
    plt.xlabel('Data' , fontsize= 18)
    plt.ylabel('Adj Price' , fontsize= 18)
    plt.legend(my_stocks.columns.values , loc = 'upper left')
    plt.show()

    # for items in my_stocks.columns.values:
    #     my_stocks[items] = my_stocks[columns].std()

def return_distribution():
    
