import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# # get all stock info from yfinance
# spy = yf.Ticker("^GSPC")
# historydf = spy.history(interval="1d", period="max")
# # print(list(historydf.axes))
# historydf.index = historydf.index.tz_localize(None)
# print(historydf)
# # save data to excel sheet
# historydf.to_excel("stockData.xlsx")


historydf = pd.read_excel("stockData.xlsx", index_col="Date")

historydf['HighLow Height abs'] = abs(historydf["High"] - historydf["Low"])


maPeriodCount = 200

historydf[f"HighLow Height MA({maPeriodCount})"] = historydf.rolling(maPeriodCount)["HighLow Height abs"].mean()

historydf[f"HighLow Height MAX({maPeriodCount})"] = historydf.rolling(maPeriodCount)["HighLow Height abs"].max()

historydf['OpenClose Height abs'] = abs(historydf["Close"] - historydf["Open"])

historydf[f"OpenClose Height MA({maPeriodCount})"] = historydf.rolling(maPeriodCount)["OpenClose Height abs"].mean()

historydf[f"OpenClose Height MAX({maPeriodCount})"] = historydf.rolling(maPeriodCount)["OpenClose Height abs"].max()

historydf["Gap Open"] = historydf["Open"] - historydf["Close"].shift(1)

historydf["applyTest"] = historydf.apply(lambda x: x["Open"] + x["Close"], 1)

print(historydf)

subsetdf = historydf[["Gap Open", "HighLow Height abs", f"HighLow Height MA({maPeriodCount})"]]
plot = subsetdf.tail(1000).plot(title="stuff")
plt.show()
