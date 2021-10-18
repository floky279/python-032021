import pandas
import requests

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/london_merged.csv")
open("london_merged.csv", 'wb').write(r.content)
df_london = pandas.read_csv("london_merged.csv")
print(df_london)
print(df_london.dtypes)
df_london["timestamp"] = pandas.to_datetime(df_london["timestamp"])
print(df_london.dtypes)
df_london["year"] = df_london["timestamp"].dt.year
print(df_london.head())

df_london = pandas.pivot_table(df_london,
                               index=["weather_code"],
                               columns=["year"],
                               aggfunc=len,
                               margins=True
                               )
print(df_london)
