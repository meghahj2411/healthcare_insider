import pandas as pd

file_path = "../data/healthcare_logs.csv"

df = pd.read_csv(file_path)

print(df.head())
