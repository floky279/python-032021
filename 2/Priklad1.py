import requests
import pandas
import numpy

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/1976-2020-president.csv") as r:
    open("1976-2020-president.csv", 'w', encoding="utf-8").write(r.text)
president_elections = pandas.read_csv("1976-2020-president.csv")
print(president_elections.head())

#Urči pořadí jednotlivých kandidátů v jednotlivých státech a v jednotlivých letech (pomocí metody rank()). Nezapomeň, že data je před použitím metody nutné seřadit a spolu s metodou rank() je nutné použít metodu groupby().

president_elections["Rank"] = president_elections.groupby(["year"])["candidatevotes"].rank(method="max", ascending=False)

print(president_elections)
print(president_elections.sort_values(["Rank"]).head())


president_elections_sorted = president_elections.sort_values(["candidatevotes", "year"])
president_elections_sorted["Rank Previous Year"] = president_elections_sorted.groupby(["candidatevotes"])["Rank"].shift()
print(president_elections_sorted.head())

president_elections_sorted["diff"]=numpy.where(president_elections_sorted["Rank"] == president_elections_sorted["Rank Previous Year"], 1, 0)
print(president_elections_sorted.head())