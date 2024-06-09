import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
data = pd.read_csv('data.csv')

# Perform basic analysis
mean_measurement1 = data['measurement1'].mean()
std_measurement1 = data['measurement1'].std()
mean_measurement2 = data['measurement2'].mean()
std_measurement2 = data['measurement2'].std()

# Print the results
print(f'Measurement 1: Mean = {mean_measurement1:.2f}, Std Dev = {std_measurement1:.2f}')
print(f'Measurement 2: Mean = {mean_measurement2:.2f}, Std Dev = {std_measurement2:.2f}')

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(data['time'], data['measurement1'], label='Measurement 1')
plt.plot(data['time'], data['measurement2'], label='Measurement 2')
plt.xlabel('Time')
plt.ylabel('Measurements')
plt.title('Time Series Data')
plt.legend()
plt.grid(True)
plt.savefig('data_plot.png')
plt.show()