import pandas as pd

print("EXPLANATION ENGINE STARTED")

# Load risk scores
risk_path = "../results/user_risk_scores.csv"
df = pd.read_csv(risk_path)

# Compute global averages for comparison
avg_accesses = df["total_accesses"].mean()
avg_unique_patients = df["unique_patients"].mean()
avg_accesses_per_day = df["avg_accesses_per_day"].mean()

explanations = []

for _, row in df.iterrows():
    if row["risk_label"] == "suspicious":
        reasons = []

        if row["total_accesses"] > 2 * avg_accesses:
            reasons.append("accessed significantly more records than average users")

        if row["unique_patients"] > 2 * avg_unique_patients:
            reasons.append("accessed an unusually high number of unique patients")

        if row["avg_accesses_per_day"] > 2 * avg_accesses_per_day:
            reasons.append("had very high access frequency per day")

        if not reasons:
            reasons.append("showed an uncommon access pattern compared to peers")

        explanation_text = "; ".join(reasons)
        explanations.append(explanation_text)
    else:
        explanations.append("normal access behavior")

# Add explanations to dataframe
df["explanation"] = explanations

# Save final explainable output
df.to_csv("../results/explainable_insider_alerts.csv", index=False)

print("EXPLANATION GENERATION COMPLETE")
print(df[df["risk_label"] == "suspicious"][["user_id", "explanation"]].head())
