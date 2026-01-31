import pandas as pd

print("SCRIPT STARTED")

# Load TAB-separated dataset
file_path = "../data/healthcare_logs.csv"
df = pd.read_csv(file_path, sep="\t")

print("COLUMNS AFTER LOADING:")
print(df.columns)

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Convert timestamp column
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Create date column
df["date"] = df["timestamp"].dt.date

# Feature engineering: user behavior summary
user_features = df.groupby("user_id").agg(
    total_accesses=("patient_id", "count"),
    unique_patients=("patient_id", "nunique"),
    active_days=("date", "nunique")
)

# Average accesses per day
user_features["avg_accesses_per_day"] = (
    user_features["total_accesses"] / user_features["active_days"]
)

# Save output
user_features.to_csv("../results/user_behavior_features.csv")

print("FEATURE ENGINEERING COMPLETE")
print(user_features.head())

