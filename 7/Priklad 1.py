

import requests
import pandas
import statsmodels.formula.api as smf

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Concrete_Data_Yeh.csv")
with open("Concrete_Data_Yeh.csv", "wb") as f:
  f.write(r.content)

df = pandas.read_csv("Concrete_Data_Yeh.csv")
print(df.head())

# Vytvoř regresní model, který bude predikovat kompresní sílu
# betonu na základě všech množství jednotlivých složek a jeho stáří.

mod = smf.ols(formula="csMPa ~ cement + slag"
                       "+ flyash + water + superplasticizer +coarseaggregate + fineaggregate + age", data=df)
res = mod.fit()
print(res.summary())

# Zhodnoť kvalitu modelu.

# Koeficient determinácie je  0.616, t.j. 61,6% je podiel variability na závislej premennej.

# Tipni si, která ze složek betonu ovlivňuje sílu betonu negativní (tj. má záporný regresní koeficient).
# Napiš, o kterou složku jde, do komentáře svého programu.

#Podľa mňa by malo íst o vodu.