import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("test.csv")

# Clean data
data = data.dropna(subset=['Age'])
data = data[~data['Age'].str.contains("Total", na=False)]
data['Indigenous'] = data['Indigenous'].replace({' ': ''}, regex=True).astype(float)
data['Non-indigenous'] = data['Non-indigenous'].replace({' ': ''}, regex=True).astype(float)

cleaned_data = data[['Age', 'Indigenous', 'Non-indigenous']]

cleaned_data.to_csv("cleaned_population_data.csv", index=False)

# Plot Indigenous population
plt.figure(figsize=(10, 6))
plt.bar(data['Age'], data['Indigenous'], color='skyblue', width=1.0, edgecolor='black')
plt.xlabel("Age Group")
plt.ylabel("Indigenous Population")
plt.title("Indigenous Population by Age Group in Australia (2011)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot Non-Indigenous population
plt.figure(figsize=(10, 6))
plt.bar(data['Age'], data['Non-indigenous'], color='salmon', width=1.0, edgecolor='black')
plt.xlabel("Age Group")
plt.ylabel("Non-Indigenous Population")
plt.title("Non-Indigenous Population by Age Group in Australia (2011)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
