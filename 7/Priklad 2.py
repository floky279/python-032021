# V souboru Fish.csv najdeš informace o rybách z rybího trhu:
#
# délku (vertikální - Length1, diagonální - Length2 a úhlopříčnou - Length3),
# výšku,
# šířku,
# živočišný druh ryby,
# hmnotnost ryby.
# Vytvoř regresní model, který bude predikovat hmnotnost ryby na základě její diagonální délky (sloupec Length2).
# Zkus přidat do modelu výšku ryby (sloupec Height)
# a porovnej, jak se zvýšila kvalita modelu. Nakonec pomocí metody target encoding zapracuj do modelu živočišný druh ryby.

import requests
import pandas
import statsmodels.formula.api as smf

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Fish.csv")
with open("Fish.csv", "wb") as f:
  f.write(r.content)

# Vytvoř regresní model, který bude predikovat hmnotnost ryby na základě její diagonální délky (sloupec Length2).
# Zkus přidat do modelu výšku ryby (sloupec Height)

df = pandas.read_csv("Fish.csv")
print(df.head())

mod = smf.ols(formula="Weight ~ Length2 + Height", data=df)

res = mod.fit()
print(res.summary())
data = pandas.DataFrame({"Length2": [32],
                         "Height": [10.5]})
print(res.predict(data))
# Pri daných hodnotách má ryba 520 g.

# a porovnej, jak se zvýšila kvalita modelu. Nakonec pomocí metody target encoding zapracuj do modelu živočišný druh ryby.
mean_species = df.groupby("Species")["Weight"].mean()
df["mean_species"] = df["Species"].map(mean_species)
mod = smf.ols(formula="Weight ~ Length2 + Height+ mean_species", data=df)
print(res.summary())

#Po pridaní živočíšneho druhu je kvalita modelu vyššia zvýšilo sa to z hodnoty 87.5% na 90%.