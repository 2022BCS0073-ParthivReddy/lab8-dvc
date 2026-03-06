import pandas as pd

# Load dataset
df = pd.read_csv("data/housing.csv")

# Take first 5000 rows
df_v1 = df.head(5000)

# Save Version 1
df_v1.to_csv("data/housing.csv", index=False)

print("Dataset Version 1 created with", len(df_v1), "rows")

