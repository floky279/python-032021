import requests
import pandas
import numpy

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
    open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)

meranie = pandas.read_csv("air_polution_ukol.csv")
print(meranie.head())

datum_merania = pandas.to_datetime(meranie["date"])
meranie["datum_merania"] = datum_merania
meranie["mesiac"] = datum_merania.dt.month
meranie["rok"] = datum_merania.dt.year

meranie = pandas.pivot_table(meranie,
                             values=["pm25"],
                             index=["mesiac"],
                             columns=["rok"],
                             aggfunc=numpy.mean)
print(meranie)
