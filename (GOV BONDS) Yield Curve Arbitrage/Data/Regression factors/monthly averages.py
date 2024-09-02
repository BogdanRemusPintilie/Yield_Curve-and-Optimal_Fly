import pandas as pd

df = pd.read_csv(r"C:\Users\Bogdan\OneDrive - University of Warwick\Desktop\Projects\(GOV BONDS) Yield Curve Arbitrage\Data\Regression factors\MORTGAGE30US.csv")

first_col = "DATE"
df[first_col] = pd.to_datetime(df[first_col], errors='coerce')
df.dropna(subset=[first_col], inplace=True)
df.set_index(first_col, inplace=True)

second_col = "MORTGAGE30US"
df[second_col] = pd.to_numeric(df[second_col], errors='coerce')
df.dropna(subset=[second_col], inplace=True)
monthly_avg = df[second_col].resample('M').mean()

monthly_avg.to_csv("Done.csv")