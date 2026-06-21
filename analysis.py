import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output folder
os.makedirs("charts", exist_ok=True)

# Load data
df = pd.read_csv("data.csv")

# Clean data
df.columns = df.columns.str.strip()
df["Questions"] = pd.to_numeric(df["Questions"], errors="coerce")
df = df.dropna(subset=["Questions"])
df["Questions"] = df["Questions"].astype(int)

# ------------------------
# DATASET OVERVIEW
# ------------------------

print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)

print(f"Topics: {len(df)}")
print(f"Categories: {df['Category'].nunique()}")
print(f"Total Questions: {df['Questions'].sum()}")

print("\nTop 5 Topics:")
print(df.nlargest(5, "Questions")[["Topic", "Questions"]])

# ------------------------
# CHART 1
# Top 10 Topics
# ------------------------

top10 = df.nlargest(10, "Questions")

plt.figure(figsize=(10, 6))
plt.barh(top10["Topic"], top10["Questions"])
plt.title("Top 10 Most Discussed Topics")
plt.xlabel("Number of Questions")
plt.tight_layout()
plt.savefig("charts/top10_topics.png")
plt.close()

# ------------------------
# CHART 2
# Category Totals
# ------------------------

cat_totals = (
    df.groupby("Category")["Questions"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
cat_totals.plot(kind="bar")
plt.title("Total Questions by Category")
plt.ylabel("Questions")
plt.tight_layout()
plt.savefig("charts/category_totals.png")
plt.close()

# ------------------------
# CHART 3
# Distribution
# ------------------------

silent = (df["Questions"] == 0).sum()
active = (df["Questions"] > 0).sum()

plt.figure(figsize=(6,6))
plt.pie(
    [silent, active],
    labels=["Silent Topics","Active Topics"],
    autopct="%1.1f%%"
)
plt.title("Silent vs Active Support Topics")
plt.savefig("charts/silent_vs_active.png")
plt.close()

print("\nCharts saved in /charts folder")
print(" - top10_topics.png")
print(" - category_totals.png")
print("Silent vs Active Support Topics.png")