import pandas
import requests
import numpy

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
    open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

meranie = pandas.read_csv("air_polution_ukol.csv")
print(meranie.head())

datum_merania = pandas.to_datetime(meranie["date"])
meranie["mesiac"] = datum_merania.dt.month
meranie["rok"] = datum_merania.dt.year

meranie_avg = meranie[((meranie["rok"] == 2019) | (meranie["rok"] == 2020)) & (meranie["mesiac"] == 1)]
meranie_avg2 = meranie_avg.groupby("rok")["pm25"].mean()

print(meranie_avg2)

#H0: Priemerné množstvo jemných častíc je rovnaká v oboch mesiacoch
#H1: Priemerné množstvo jemných častíc v oboch mesiacoch je rôzne

from scipy.stats import mannwhitneyu
x = meranie_avg[meranie_avg["rok"] == 2020]["pm25"]
y = meranie_avg[meranie_avg["rok"] == 2019]["pm25"]
print(mannwhitneyu(x, y))

# P-hodnota je 1,1%, čiže pri hladine významnosti 5 % sa H0 hypotéza zamieta.
#Tvrdíme teda, že priemerné množstvo jemných častíc v oboch mesiacoch je rôzne.