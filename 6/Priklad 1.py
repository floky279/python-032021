import statistics

import requests
import pandas
with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/psenice.csv") as r:
  open("psenice.csv", 'w', encoding="utf-8").write(r.text)

data = pandas.read_csv("psenice.csv")
print(data.head())

#H0: Priemery dlzky zrn je rovnaka pre obe zrna
#H1: Priemery dlzky zrn nie je rovnaka

from scipy.stats import mannwhitneyu
from statistics import mean


x = data["Rosa"]
y = data["Canadian"]

print(mannwhitneyu(x, y))

# P- hodnota je 352 %, ktoré je vacsie ako 5%, cize v tomto pripade sa H0 hypoteza nezamieta.
# Tvrdíme teda, že priemery dlžok zrna je rovnaká




