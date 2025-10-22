import time

import dask.dataframe as dd
import polars as pl
import numpy as np
import os
import pandas as pd

filename = "bigfile_polars.csv"

start = time.time()
df = pd.read_csv(filename)
mean = df["value"].mean()
print("Pandas mean:", mean)
print("Czas:", time.time() - start)


start = time.time()
df = pl.read_csv(filename)
mean = df["value"].mean()
print("Polars mean:", mean)
print("Czas:", time.time() - start)

# Lazy scan ( nie ładuje cąlego pliku do pamięci)
# wykona zadanie dopiery gdy dane będą potrzebne
start = time.time()
df = pl.scan_csv(filename)
mean = df.select(pl.col("value").mean()).collect()
print("Polars mean(scan):", mean)
print("Czas:", time.time() - start)

# dasotrzebuje pyarrow
start = time.time()
df = dd.read_csv(filename)
mean = df["value"].mean().compute()
print("Dask mean:", mean)
print("Czas:", time.time() - start)

# Pandas mean: 5001.6439352
# Czas: 3.8495776653289795
# Polars mean: 5001.6439352
# Czas: 0.5321919918060303
# Polars mean(scan): shape: (1, 1)
# ┌─────────────┐
# │ value       │
# │ ---         │
# │ f64         │
# ╞═════════════╡
# │ 5001.643935 │
# └─────────────┘
# Czas: 0.3783261775970459
# Dask mean: 5001.6439352
# Czas: 4.01762580871582