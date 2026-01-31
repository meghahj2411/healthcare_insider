import pandas as pd
from sklearn.ensemble import IsolationForest

print("ISOLATION FOREST STARTED")

# Load user behavior features
features_path = "../results/user_behavior_features.csv"
df = pd.read_csv(features_path)

# Select features for ML
X = df[["total_accesses", "unique_patients", "avg_accesses_per_day"]]

# Train Isolation Forest
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

model.fit(X)

# Predict anomalies (-1 = anomaly, 1 = normal)
df["anomaly_flag"] = model.predict(X)

# Convert to readable labels
df["risk_label"] = df["anomaly_flag"].apply(
    lambda x: "suspicious" if x == -1 else "normal"
)

# Save results
df.to_csv("../results/user_risk_scores.csv", index=False)

print("ISOLATION FOREST COMPLETE")
print(df["risk_label"].value_counts())
