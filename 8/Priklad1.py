import pandas
import requests
import matplotlib.pyplot as plt
import yfinance as yf



from statsmodels.tsa.ar_model import AutoReg
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.seasonal import seasonal_decompose


# Pomocí modulu yfinance, který jsme používali v 5. lekci,
# stáhni ceny akcií společnosti Cisco (používají "Ticker" CSCO) za posledních 5 let.
# Dále pracuj s cenami akcie v závěru obchodního dne, tj. použij sloupec "Close".

csco = yf.Ticker("CSCO")
csco_df = csco.history(period="5y")
csco_close =csco_df["Close"]

#previedla som dáta z Tickeru pre lepši prehľad
#csco_df.to_csv("aa.csv")

# Zobraz si graf autokorelace a podívej se, jak je hodnota ceny závislná na svých vlastních hodnotách v minulosti.
# Zkus použít AR model k predikci cen akcie na příštích 5 dní.
# Zobraz v grafu historické hodnoty (nikoli celou řadu, ale pro přehlednost např. hodnoty za posledních 50 dní)
# a tebou vypočítanou predikci.

print(csco_df["Close"].autocorr(lag=1))

plot_acf(csco_df["Close"])
plt.show()

df_50 = csco_df.tail(50)
#print(df_50["Close"])
model = AutoReg(df_50["Close"], lags=5, trend="t", seasonal=True, period=12)
model_fit = model.fit()


predictions = model_fit.predict(start=csco_df.shape[0], end=csco_df.shape[0] + 5)
df_forecast = pandas.DataFrame(predictions, columns=["Prediction"])
df_with_prediction = pandas.concat([csco_df, df_forecast])
df_with_prediction[["Close", "Prediction"]].plot()
plt.show()