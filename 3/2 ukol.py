# Chceme ke každému zvířeti vytvořit popisek na tabulku do zoo.
# Popisek bude využívat sloupců title (název zvířete), food (typ stravy),
# food_note (vysvětlující doplněk ke stravě) a description (jak zvíře poznáme).
# Napiš funkci popisek, která bude mít jeden parametr radek. Funkce spojí informace dohromady.
# Následně použijte metodu apply, abyste vytvořili nový sloupec s tímto popiskem.

import pandas
import requests

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)

popisek_zvirat = pandas.read_csv("lexikon-zvirat.csv", sep=";")
popisek_zvirat = popisek_zvirat.dropna(how="all", axis="columns")
popisek_zvirat = popisek_zvirat.dropna(how="all", axis="rows")
popisek_zvirat = popisek_zvirat.set_index("id")


# print(popisek_zvirat)

def popisek(radek):
    title = popisek_zvirat.title + "preferuje následující typ stravy:" + popisek_zvirat.food + "" + popisek_zvirat.food_note
    description = "Jak toto zvíře poznáme:" + popisek_zvirat.description
    informace = title + description
    print(informace)

popisek_zvirat["popisek"] = popisek_zvirat.apply(popisek, axis=0)

print(popisek_zvirat)
