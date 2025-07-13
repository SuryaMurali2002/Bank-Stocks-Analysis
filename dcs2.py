# from pandas_datareader import data, wb # will have to use yfinance to read this data from yahoo api
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import yfinance as yf
import datetime

#setting up starting and ending date.
start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)

#downloading data for each bank from Yahoo
BAC = yf.download('BAC', start=start, end=end)
C = yf.download('C', start=start, end=end)
GS = yf.download('GS', start=start, end=end)
JPM = yf.download('JPM', start=start, end=end)
MS = yf.download('MS', start=start, end=end)
WFC = yf.download('WFC', start=start, end=end)

#making a dictionary with the data for easy access
bank_stocks = {
    'BAC': BAC,
    'C': C,
    'GS': GS,
    'JPM': JPM,
    'MS': MS,
    'WFC': WFC
}

# for name, df in bank_stocks.items():
#     print(f"{name}:")
#     print(df.head())


# Now i want to make a dataframe with closing prices of each bank stock

closing_prices = pd.DataFrame()
for ticker in bank_stocks:
    closing_prices[ticker] = bank_stocks[ticker]['Close']

# print(closing_prices.head())

#now we are plotting the closing prices for all the bank stocks from 2006 to 2016
# sns.lineplot(data=closing_prices)
# plt.title('Bank Closing Prices (2006–2016)')
# plt.xlabel('years')
# plt.ylabel('closing prices')
# plt.show()

# how to calculate return for each bank using the closing prices dataframe.
return_price = []
for i in range(1, len(closing_prices)):
    row = (closing_prices.iloc[i] - closing_prices.iloc[i-1])/closing_prices.iloc[i-1]
    return_price.append(row)

return_price = pd.DataFrame(return_price)
return_price.index = closing_prices.index[1:]
# print(return_price.head())
# sns.pairplot(data=return_price)
# plt.xlabel('banks')
# plt.ylabel('returns')
# plt.show()

returns_devn = return_price.std()
# print(returns_devn)

## std devn by year
std_dev_by_year = return_price.groupby(by=return_price.index.year)
# print(std_dev_by_year.std())

corrmatrixofbanks = return_price.corr()
# print(corrmatrixofbanks)
# corrheatmap = sns.heatmap(corrmatrixofbanks, annot=True, cmap='coolwarm')
# plt.show()

#30 day window Moving avergae dataframe

MA_df = pd.DataFrame()
for each_bank in closing_prices.columns:
    MA_df[each_bank] = closing_prices[each_bank].rolling(window=30).mean()

# print(MA_df) # to check the DF

# plotting MA vs closing prices.

# plt.figure(figsize=(12,6))
# closing_prices['BAC'].plot(label='BAC Close Price')
# MA_df['BAC'].plot(label='BAC 30-Day MA')
# plt.xlabel('Date')
# plt.ylabel('Price (USD)')
# plt.title('BAC Close Price vs 30-Day Moving Average')
# plt.legend()
# plt.grid(True)
# plt.show()


#highest closing price for each bank
max_dates = closing_prices.idxmax()
# print(max_dates)

# print(closing_prices.describe())


#similarly we can do SMA (Simple MA) and bollinger bands ( SMA_ofn_days +- 2* Rolling sd of n days)







