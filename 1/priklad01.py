import pandas
import requests

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/titanic.csv")
open("titanic.csv", 'wb').write(r.content)

df_titanic = pandas.read_csv("titanic.csv")
print(df_titanic.columns)
print(df_titanic)
df_titanic = pandas.pivot_table(df_titanic,
                                index=["Pclass",
                                       "Sex",
                                       "Survived"],
                                values="Name",
                                aggfunc=len,
                                margins=True)
print(df_titanic)

