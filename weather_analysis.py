#---------------------------------
# step1: import libraries
#---------------------------------

import pandas as pd
import matplotlib as plt
import seaborn as sns
 
# For Better visualization
plt.style.use("seaborn-v0_8")

#---------------------------------
# step2: Load Files
#---------------------------------


file_path = r"C:\Users\Mitali\OneDrive\Desktop\New folder\weather_Analysis\weather_data.csv"
df = pd.read_csv(file_path)

#---------------------------------
# Step3: Display original data
#---------------------------------

# Conert data column to datetime
df['date'] = pd.to_datetime(df['date'])

print("===\nOriginal Data\n===")
print(df.head())
print(df.info())
print(df.describe())

#---------------------------------
# Step4: Handling missing values
#---------------------------------

df.filling({
    "precipitation":0,
    "Windspeed":df["Windspeed"].mean(),
    "Humidity":df["Humidity"].mean(),
},inplace=True)

#----------------------------------
#Step5: Add Missing column (Month,Day)
#----------------------------------

df["Month"] = df["date"].dt.month
df["Day"] = df["date"].dt.day

#----------------------------------
# Step6: Data Analysis
#----------------------------------

#1. Average Temperature and Humidity 
avg_temp = df["Temperature"].mean()
avg_humidity = df["Humidity"].mean()
print(f'Average temperature: {avg_temp:.2f}C')
print(f'Average humidity: {avg_humidity:.2f}%')

#2. Frequency of weather conditions
Condition_freq = df["Condition"]
print("\n===\nfrequency===")
print(Condition_freq.value_counts())

#-----------------------------------
# step7: Data Visualization
#-----------------------------------

#1. Temperature distribution
plt.figure(figsize=(10,5))
plt.plot(df["date"],df["Temperature"],marker="o")
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#2. Humidity distribution
plt.figure(figsize=(10,5))
plt.plot(df["date"],df["Humidity"],marker="o",color="orange")
plt.title("Daily Humidity Trend")
plt.xlabel("Date")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#3. Condition Frequency
plt.figure(figsize=(7,5))
sns.countplot(x="Condition",data=df)
plt.title("Frequency of Weather Conditions")
plt.xlabel("Condition")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#4. Temperature vs Humidity
plt.figure(figsize=(7,5))
plt.plot(df["Temperature"],df["Humidity"],marker="o")
plt.title("Daily Temperature trend")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#5. Correlation Heatmap
plt.figure(figsize=(7,5))
sns.heatmap(df[["Temperature","Humidity","Windspeed","precipitation"]].corr(),annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
