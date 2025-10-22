import time
import numpy as np
import pandas as pd
import polars as pl

# pip install polars

# Dane testowe - 5 milionów wierszy
N = 10_000_000
a = np.random.randint(0, 100, size=N)
b = np.random.rand(N)

# --- Pandas ----
df_pd = pd.DataFrame({"a": a, "b": b})

start = time.perf_counter()
mean_pd = df_pd[df_pd["a"] > 50]["b"].mean()
time_pd = time.perf_counter() - start

# --- Polars ----
df_pl = pl.DataFrame({"a": a, "b": b})

start = time.perf_counter()
mean_pl = df_pl.filter(pl.col("a") > 50)["b"].mean()
time_pl = time.perf_counter() - start

print(f"Pandas: {time_pd:.4f} s, wynik: {mean_pd}")
print(f"Polars: {time_pl:.4f} s, wynik: {mean_pl}")