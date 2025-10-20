import pandas as pd
import numpy as np

# Load the dataset
file_path = ('/Users/dineosmacbook/Downloads/hexsoftwares files/flight_data_2024_sample.csv')
df = pd.read_csv(file_path)

# 1. Drop columns with too many missing values
# 'cancellation_code' is mostly missing — we’ll drop it
df.drop(columns=['cancellation_code'], inplace=True)

# 2. Handle missing values for numeric columns
# Fill with median (less affected by outliers)
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].apply(lambda x: x.fillna(x.median()))

# 3. Handle missing values for categorical columns (if any)
categorical_cols = df.select_dtypes(include=['object']).columns
df[categorical_cols] = df[categorical_cols].fillna('Unknown')

# 4. Convert date column to datetime
df['fl_date'] = pd.to_datetime(df['fl_date'], errors='coerce')

# 5. Remove duplicates
df.drop_duplicates(inplace=True)

# 6. Standardize column names (lowercase, underscores)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 7. Optional: Remove cancelled or diverted flights for analysis
df_clean = df[(df['cancelled'] == 0) & (df['diverted'] == 0)]

# 8. Reset index
df_clean.reset_index(drop=True, inplace=True)

# 9. Save cleaned version
df_clean.to_csv('/Users/dineosmacbook/Downloads/hexsoftwares files/flight_data_2024_sample.csv', index=False)

print("✅ Data cleaned successfully!")
print(df_clean.info())
print(df_clean.head())
