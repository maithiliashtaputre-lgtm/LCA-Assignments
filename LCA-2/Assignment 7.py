import pandas as pd

df = pd.read_csv("/content/Titanic-Dataset.csv")
print(df)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nStatistical Summary:")
print(df.describe())

df.describe()

import matplotlib.pyplot as plt

counts = df["Pclass"].value_counts().sort_index()

plt.bar(counts.index, counts.values)

plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.title("Number of Passengers in Each Class")
plt.xticks([1, 2, 3])

plt.show()

print(counts)
print(type(counts))
print(counts.index, counts.values)

mean_fare = df[df["Pclass"] == 1]["Fare"].mean()

counts = df["Survived"].value_counts().sort_index()
plt.bar(counts.index, counts.values)

plt.xlabel("Survival Status")
plt.ylabel("Number of Passengers")
plt.title("Titanic Passenger Survival")

plt.xticks([0, 1], ["Not Survived", "Survived"])

plt.show()

counts = df.groupby(["Survived", "Sex"]).size().unstack()

print(counts)

counts.plot(kind="bar")

plt.xlabel("Survival Status")
plt.ylabel("Number of Passengers")
plt.title("Titanic Survival by Gender")

plt.xticks([0, 1], ["Not Survived", "Survived"], rotation=0)

plt.show()

data = df.dropna(subset=["Age", "Fare"])

plt.scatter(data["Age"], data["Fare"])

plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Age vs Fare in Titanic Dataset")

plt.show()

dfs=df.sort_values(by="Fare")

df[df["Fare"]==0]

dfs.tail(2)

data = df.dropna(subset=["Pclass", "Fare"])

plt.scatter(data["Pclass"], data["Fare"])

plt.xlabel("Passenger Class")
plt.ylabel("Fare")
plt.title("Passenger Class vs Fare")

plt.xticks([1, 2, 3])
plt.grid(True)

plt.show()

data = df.dropna(subset=["Pclass", "Age"])

plt.scatter(data["Pclass"], data["Age"])

plt.xlabel("Passenger Class")
plt.ylabel("Age")
plt.title("Passenger Class vs Age")

plt.xticks([1, 2, 3])
plt.grid(True)

plt.show()

avg_fare = df.groupby("Pclass")["Fare"].mean()

plt.plot(avg_fare.index, avg_fare.values, marker="o")

plt.xlabel("Passenger Class")
plt.ylabel("Average Fare")
plt.title("Average Fare by Passenger Class")

plt.xticks([1, 2, 3])
plt.grid(True)

plt.show()