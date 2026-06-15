import pandas as pd
df = pd.read_csv("sales_data.csv")
df = df.dropna(subset=["Name", "Sales"])
df["Name"] = df["Name"].str.title()
df["Region"] = df["Region"].str.title()
df["Sales"] = df["Sales"].astype(float)

df["Bonus"] = df["Sales"] * 0.10
df.to_excel("sales_report.xlsx", index = False)
print("Report saved to sales_report.xlxs")
