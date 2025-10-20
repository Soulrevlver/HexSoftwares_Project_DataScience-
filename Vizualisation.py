import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
file_path = ('/Users/dineosmacbook/Downloads/hexsoftwares files/flight_data_2024_sample.csv')
df = pd.read_csv(file_path)

# Set Seaborn style
sns.set(style="whitegrid", palette="muted", font_scale=1.1)

# 1️⃣ Distribution of Departure Delays
plt.figure(figsize=(8,5))
sns.histplot(df['dep_delay'], bins=50, kde=True, color='steelblue')
plt.title("Distribution of Departure Delays (minutes)")
plt.xlabel("Departure Delay (min)")
plt.ylabel("Number of Flights")
plt.show()

# 2️⃣ Distribution of Arrival Delays
plt.figure(figsize=(8,5))
sns.histplot(df['arr_delay'], bins=50, kde=True, color='salmon')
plt.title("Distribution of Arrival Delays (minutes)")
plt.xlabel("Arrival Delay (min)")
plt.ylabel("Number of Flights")
plt.show()

# 3️⃣ Relationship between Distance and Arrival Delay
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='distance', y='arr_delay', alpha=0.3, color='purple')
plt.title("Distance vs Arrival Delay")
plt.xlabel("Flight Distance (miles)")
plt.ylabel("Arrival Delay (min)")
plt.show()

# 4️⃣ Correlation Heatmap
plt.figure(figsize=(10,8))
numeric_df = df.select_dtypes(include=['float64', 'int64'])
corr = numeric_df.corr()
sns.heatmap(corr, cmap='coolwarm', annot=False)
plt.title("Correlation Heatmap of Numeric Features")
plt.show()

# 5️⃣ Top 10 Busiest Origin Airports
plt.figure(figsize=(10,5))
top_origins = df['origin'].value_counts().head(10)
sns.barplot(x=top_origins.index, y=top_origins.values, palette="Blues_r")
plt.title("Top 10 Busiest Origin Airports")
plt.xlabel("Airport")
plt.ylabel("Number of Flights")
plt.show()

# 6️⃣ Average Arrival Delay by Day of Week
plt.figure(figsize=(8,5))
sns.barplot(x='day_of_week', y='arr_delay', data=df, palette="crest")
plt.title("Average Arrival Delay by Day of Week")
plt.xlabel("Day of Week (1=Mon, 7=Sun)")
plt.ylabel("Average Arrival Delay (min)")
plt.show()

# 7️⃣ Average Delay by Month
plt.figure(figsize=(8,5))
sns.barplot(x='month', y='arr_delay', data=df, palette="flare")
plt.title("Average Arrival Delay by Month")
plt.xlabel("Month")
plt.ylabel("Average Arrival Delay (min)")
plt.show()

