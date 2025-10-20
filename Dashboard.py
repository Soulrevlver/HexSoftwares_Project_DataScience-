import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
file_path = ('/Users/dineosmacbook/Downloads/hexsoftwares files/flight_data_2024_sample.csv')
df = pd.read_csv(file_path)

sns.set(style="whitegrid", palette="muted", font_scale=1.1)

# 1️⃣ Average Arrival Delay by Airline
plt.figure(figsize=(10,6))
avg_delay_airline = (
    df.groupby('op_unique_carrier')['arr_delay']
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)
sns.barplot(x='arr_delay', y='op_unique_carrier', data=avg_delay_airline, palette="viridis")
plt.title("Average Arrival Delay by Airline")
plt.xlabel("Average Arrival Delay (minutes)")
plt.ylabel("Airline Code")
plt.show()

# 2️⃣ Average Departure Delay by Airline
plt.figure(figsize=(10,6))
avg_dep_delay = (
    df.groupby('op_unique_carrier')['dep_delay']
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)
sns.barplot(x='dep_delay', y='op_unique_carrier', data=avg_dep_delay, palette="magma")
plt.title("Average Departure Delay by Airline")
plt.xlabel("Average Departure Delay (minutes)")
plt.ylabel("Airline Code")
plt.show()

# 3️⃣ Average Arrival Delay by Origin State
plt.figure(figsize=(12,6))
avg_delay_origin_state = (
    df.groupby('origin_state_nm')['arr_delay']
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)
sns.barplot(x='arr_delay', y='origin_state_nm', data=avg_delay_origin_state, palette="coolwarm")
plt.title("Average Arrival Delay by Origin State")
plt.xlabel("Average Arrival Delay (minutes)")
plt.ylabel("Origin State")
plt.show()

# 4️⃣ Average Arrival Delay by Destination State
plt.figure(figsize=(12,6))
avg_delay_dest_state = (
    df.groupby('dest_state_nm')['arr_delay']
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)
sns.barplot(x='arr_delay', y='dest_state_nm', data=avg_delay_dest_state, palette="crest")
plt.title("Average Arrival Delay by Destination State")
plt.xlabel("Average Arrival Delay (minutes)")
plt.ylabel("Destination State")
plt.show()

# 5️⃣ Flights per Airline
plt.figure(figsize=(10,5))
flight_count = df['op_unique_carrier'].value_counts().reset_index()
flight_count.columns = ['Airline', 'Flights']
sns.barplot(x='Airline', y='Flights', data=flight_count, palette="Blues_d")
plt.title("Total Flights per Airline")
plt.xlabel("Airline Code")
plt.ylabel("Number of Flights")
plt.show()

# 6️⃣ Boxplot: Distribution of Arrival Delays by Airline
plt.figure(figsize=(12,6))
sns.boxplot(data=df, x='op_unique_carrier', y='arr_delay', palette="Set3")
plt.title("Distribution of Arrival Delays by Airline")
plt.xlabel("Airline Code")
plt.ylabel("Arrival Delay (minutes)")
plt.show()

