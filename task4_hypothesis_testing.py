import pandas as pd
from scipy.stats import ttest_ind

# Load dataset
df = pd.read_csv("customer_purchases_raw.csv")

# Create age groups
df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[17, 25, 35, 45, 100],
    labels=["18-25", "26-35", "36-45", "46+"]
)

# Filter groups
group_18_25 = df[df["Age_Group"] == "18-25"]["Purchase_Amount"]
group_36_45 = df[df["Age_Group"] == "36-45"]["Purchase_Amount"]

# Perform independent t-test
t_stat, p_value = ttest_ind(group_18_25, group_36_45, equal_var=False)

print("T-Statistic:", t_stat)
print("P-Value:", p_value)

# Interpretation
if p_value < 0.05:
    print("Reject the null hypothesis: Significant difference exists.")
else:
    print("Fail to reject the null hypothesis: No significant difference.")
