import requests
import pandas
import statistics
import numpy
import seaborn
from matplotlib import pyplot as plt

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
open("crypto_prices.csv", "wb").write(r.content)
crypto_prices = pandas.read_csv("crypto_prices.csv")
crypto_prices["Close_next"] = crypto_prices.groupby(["Name"])["Close"].shift(1)
crypto_prices["change"] = crypto_prices["Close"]/crypto_prices["Close_next"]*100-100
crypto_prices = crypto_prices.dropna(subset=["change"])
crypto_prices["pct"] = crypto_prices.groupby(["Name"])["Close"].pct_change()


crypto_prices_pivot = pandas.pivot_table(crypto_prices, index="Date", columns="Symbol", values="pct", aggfunc=numpy.sum)
print(crypto_prices_pivot)


def check_radek(radek):
    radek = radek.sort_values(ascending=False)
    radek = radek.iloc[1]
    return radek


maximum = 0
maximum_index = None
for index, radek in crypto_prices_pivot.corr().iterrows():
    result = check_radek(radek)
    if result > maximum:
        maximum = result
        maximum_index = index
print(maximum)
print(maximum_index)
max_sloupec = crypto_prices_pivot.corr()[maximum_index]
print(max_sloupec[max_sloupec == maximum])

seaborn.jointplot("USDT", "USDC", crypto_prices_pivot, kind='scatter', color='seagreen')
plt.show()
seaborn.jointplot("BTC", "ADA", crypto_prices_pivot, kind='scatter', color='seagreen')
plt.show()

XMR = crypto_prices[crypto_prices["Symbol"] == "XMR"]["pct"] + 1
XMR = XMR.tolist()[1:]
print(statistics.geometric_mean(XMR))