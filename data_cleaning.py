import pandas as pd

df = pd.read_csv("marketing_campaign.csv", sep=';')

print("Original Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())

df = df.dropna()

df = df.drop_duplicates()

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

df['dt_customer'] = pd.to_datetime(df['dt_customer'], format='%d-%m-%Y')

df['income'] = df['income'].astype(int)

df['age'] = 2025 - df['year_birth']

df.to_csv("cleaned_marketing_campaign.csv", index=False)

print("\n✅ Data cleaning complete.")
print("New Shape:", df.shape)
print("Cleaned file saved as 'cleaned_marketing_campaign.csv'")
