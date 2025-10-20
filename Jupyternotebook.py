# ===============================
#  FLIGHT DATA ANALYSIS PROJECT
# ===============================

# --- STEP 1: Import Libraries ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", palette="muted", font_scale=1.1)

# --- STEP 2: Load Dataset ---
file_path = ('/Users/dineosmacbook/Downloads/hexsoftwares files/flight_data_2024_sample.csv')
df = pd.read_csv(file_path)

print("✅ Raw data loaded successfully!")
print(df.shape)
df.head()


# --- STEP 3: Data Cleaning ---
# Drop columns with excessive missing data
df.drop(columns=['cancellation_code'], inplace=True)

# Fill missing numeric values with median
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].apply(lambda x: x.fillna(x.median()))

# Fill missing categorical values with 'Unknown'
categorical_cols = df.select_dtypes(include=['object']).columns
df[categorical_cols] = df[categorical_cols].fillna('Unknown')

# Convert date column
df['fl_date'] = pd.to_datetime(df['fl_date'], errors='coerce')

# Remove duplicates and cancelled/diverted flights
df.drop_duplicates(inplace=True)
df = df[(df['cancelled'] == 0) & (df['diverted'] == 0)]

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

df.reset_index(drop=True, inplace=True)
print("✅ Data cleaned successfully!")
df.info()


# --- STEP 4: Save Cleaned Data ---
df.to_csv("flight_data_2024_cleaned.csv", index=False)


# --- STEP 5: Basic Visualizations ---
plt.figure(figsize=(8,5))
sns.histplot(df['dep_delay'], bins=50, kde=True, color='steelblue')
plt.title("Distribution of Departure Delays (minutes)")
plt.xlabel("Departure Delay")
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(df['arr_delay'], bins=50, kde=True, color='salmon')
plt.title("Distribution of Arrival Delays (minutes)")
plt.xlabel("Arrival Delay")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='distance', y='arr_delay', alpha=0.3, color='purple')
plt.title("Distance vs Arrival Delay")
plt.xlabel("Flight Distance (miles)")
plt.ylabel("Arrival Delay (min)")
plt.show()

plt.figure(figsize=(10,8))
sns.heatmap(df.select_dtypes(include=[np.number]).corr(), cmap='coolwarm', annot=False)
plt.title("Correlation Heatmap")
plt.show()

# --- STEP 6: Categorical Comparisons ---
plt.figure(figsize=(10,6))
avg_delay_airline = df.groupby('op_unique_carrier')['arr_delay'].mean().sort_values(ascending=False).reset_index()
sns.barplot(x='arr_delay', y='op_unique_carrier', data=avg_delay_airline, palette="viridis")
plt.title("Average Arrival Delay by Airline")
plt.xlabel("Average Delay (min)")
plt.ylabel("Airline")
plt.show()

plt.figure(figsize=(12,6))
avg_delay_state = df.groupby('origin_state_nm')['arr_delay'].mean().sort_values(ascending=False).reset_index()
sns.barplot(x='arr_delay', y='origin_state_nm', data=avg_delay_state, palette="coolwarm")
plt.title("Average Arrival Delay by Origin State")
plt.xlabel("Average Delay (min)")
plt.ylabel("Origin State")
plt.show()


# --- STEP 7: Advanced Visuals (Pairplots + Correlations) ---
pair_cols = ['dep_delay', 'arr_delay', 'air_time', 'distance']
sns.pairplot(df[pair_cols].dropna(), diag_kind='kde', corner=True)
plt.suptitle("Pairwise Relationships Between Flight Variables", y=1.02)
plt.show()

top5_airlines = df['op_unique_carrier'].value_counts().index[:5]
subset = df[df['op_unique_carrier'].isin(top5_airlines)]

sns.pairplot(
    subset,
    vars=['dep_delay', 'arr_delay', 'air_time', 'distance'],
    hue='op_unique_carrier',
    diag_kind='kde',
    corner=True,
    palette='husl'
)
plt.suptitle("Flight Variables by Top 5 Airlines", y=1.03)
plt.show()

# Correlation heatmaps per airline
key_vars = ['dep_delay', 'arr_delay', 'air_time', 'distance', 'taxi_out', 'taxi_in']
fig, axes = plt.subplots(1, len(top5_airlines), figsize=(20,5))
for ax, airline in zip(axes, top5_airlines):
    corr = subset[subset['op_unique_carrier'] == airline][key_vars].corr()
    sns.heatmap(corr, cmap='coolwarm', annot=False, ax=ax)
    ax.set_title(f"{airline}")
plt.suptitle("Correlation by Airline", fontsize=14, y=1.05)
plt.tight_layout()
plt.show()


# --- STEP 8: Summary Dashboard ---
print("📊 Summary Statistics:")
print(df[['dep_delay', 'arr_delay', 'air_time', 'distance']].describe())

df['route'] = df['origin'] + " → " + df['dest']

# Top routes by delay
top_routes = (
    df.groupby('route')['arr_delay']
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
print("\n🛫 Top 10 Routes with Highest Average Arrival Delays:")
print(top_routes)

# Airline performance summary
airline_perf = (
    df.groupby('op_unique_carrier')
    .agg(
        total_flights=('op_unique_carrier', 'count'),
        avg_dep_delay=('dep_delay', 'mean'),
        avg_arr_delay=('arr_delay', 'mean'),
        avg_distance=('distance', 'mean'),
    )
    .sort_values(by='avg_arr_delay', ascending=False)
    .reset_index()
)
print("\n🏆 Airline Performance Summary:")
print(airline_perf.head(10))

# Visualization: Top 10 Delayed Routes
plt.figure(figsize=(12,6))
sns.barplot(x='arr_delay', y='route', data=top_routes, palette='flare')
plt.title("Top 10 Routes with Highest Average Arrival Delays")
plt.xlabel("Average Arrival Delay (min)")
plt.ylabel("Route")
plt.show()

# Visualization: Monthly Delay Trends
avg_delay_month = df.groupby('month')['arr_delay'].mean().reset_index()
plt.figure(figsize=(8,5))
sns.lineplot(data=avg_delay_month, x='month', y='arr_delay', marker='o', color='darkred')
plt.title("Average Arrival Delay by Month")
plt.xlabel("Month")
plt.ylabel("Average Delay (min)")
plt.grid(True)
plt.show()

print("\n✅ Dashboard analysis complete!")
