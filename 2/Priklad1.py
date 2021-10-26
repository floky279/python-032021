import requests
import pandas
import numpy

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/1976-2020-president.csv") as r:
    open("1976-2020-president.csv", 'w', encoding="utf-8").write(r.text)
president_elections = pandas.read_csv("1976-2020-president.csv")
print(president_elections.head())

president_elections["Rank"] = president_elections.groupby(["state", "year"])["candidatevotes"].rank(ascending=False)

president_elections_sorted = president_elections.sort_values(["Rank", "state", "party_simplified", "year"])
president_elections_sorted["previous_election_party"] = president_elections_sorted.groupby(["Rank"])["party_simplified"].shift()


president_elections_sorted["diff"] = numpy.where(president_elections_sorted["party_simplified"] == president_elections_sorted["previous_election_party"], 0, 1)
print(president_elections_sorted.head())
