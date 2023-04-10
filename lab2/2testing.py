import pandas as pd


# 1
data = pd.read_csv("sp500hst.txt", sep=",", names=[
                   "date", "ticker", "open", "high", "low", "close", "volume"], parse_dates=["date"])
print(data.head())

# 2
avg_val = data.iloc[:, 3:7].mean()
print("\nСредние значения для столбцов 3-6:\n", avg_val)

# 3
data["month"] = data["date"].dt.month
print("\nDataFrame с добавленным столбцом 'month':\n", data.head())

# 4
volume_by_ticker = data.groupby("ticker")["volume"].sum()
print("\nCуммарный объем торгов для для одинаковых значений тикеров:\n", volume_by_ticker)

# 5
tickers = pd.read_csv("sp_data2.csv", sep=";", names=[
                      'ticker', 'company', 'percentage'])
data_with_tickers = pd.merge(data, tickers, on="ticker", how="left")
missing_tickers = data_with_tickers.loc[data_with_tickers["company"].isnull(
), "ticker"].unique()
if len(missing_tickers) > 0:
    print(
        f"Не удалось найти информацию о компании для тикеров: {', '.join(missing_tickers)}")
print(data_with_tickers.head())
