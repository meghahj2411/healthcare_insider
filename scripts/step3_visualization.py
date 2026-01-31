import pandas as pd
import matplotlib.pyplot as plt

print("VISUALIZATION STARTED")

# Load the feature-engineered data
features_path = "../results/user_behavior_features.csv"
df = pd.read_csv(features_path)

# Plot distribution of total accesses per user
plt.figure()
plt.hist(df["total_accesses"], bins=30)
plt.xlabel("Total Accesses per User")
plt.ylabel("Number of Users")
plt.title("Distribution of User Access Behavior")

plt.show()
