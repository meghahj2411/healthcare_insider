import pandas as pd

print("RISK SEVERITY ENGINE STARTED")

# Load explainable alerts
input_path = "../results/explainable_insider_alerts.csv"
df = pd.read_csv(input_path)

# Compute global statistics
avg_accesses = df["total_accesses"].mean()
avg_unique_patients = df["unique_patients"].mean()

risk_levels = []

for _, row in df.iterrows():
    if row["risk_label"] == "normal":
        risk_levels.append("LOW")
    else:
        score = 0

        if row["total_accesses"] > 2 * avg_accesses:
            score += 2
        elif row["total_accesses"] > avg_accesses:
            score += 1

        if row["unique_patients"] > 2 * avg_unique_patients:
            score += 2
        elif row["unique_patients"] > avg_unique_patients:
            score += 1

        # Assign severity
        if score >= 4:
            risk_levels.append("HIGH")
        elif score >= 2:
            risk_levels.append("MEDIUM")
        else:
            risk_levels.append("LOW")

# Add risk severity
df["risk_severity"] = risk_levels

# Save final enriched output
df.to_csv("../results/final_insider_risk_report.csv", index=False)

print("RISK SEVERITY ASSIGNMENT COMPLETE")
print(df["risk_severity"].value_counts())
