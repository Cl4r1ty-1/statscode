import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x1, y1 = 2008,450
x2, y2 = 2013,-500

# Calculate slope (m) and y-intercept (b) for the line of best fit
m = (y2 - y1) / (x2 - x1)
b = y1 - m * x1

# Load the data
time_data = pd.read_csv("time.csv")
# Convert the 'Year' column to datetime format if necessary
time_data['Year'] = time_data['Year'].astype(int)

# Generate x values within the range of the data for plotting the line of best fit
x_values = np.array(time_data["Year"])
line_of_best_fit = m * x_values + b

# Plot the time series for ice mass in Antarctica
plt.figure(figsize=(10, 6))
# Plot Ice Mass over time
plt.plot(time_data['Year'], time_data['Ice Mass Change'], label='Change', color='blue')

# Plot the line of best fit

# Customize the plot
plt.xlabel("Year")
plt.ylabel("Change in Ice Mass (Gigatonnes)")
plt.title("Change in Ice Mass in Antarctica Over Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
