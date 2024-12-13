import numpy as np
import matplotlib.pyplot as plt

temperature_matrix = np.random.randint(15, 30, size=(7,3))

mean_by_city = np.mean(temperature_matrix, axis=0)
max_temp_by_day = np.max(temperature_matrix, axis=1)
min_temp_by_city = np.min(temperature_matrix, axis=0)

noice = np.random.uniform(-0.5, 0.5, size=temperature_matrix.shape)
temperature_matrix_noice = temperature_matrix + noice

mean_by_city_noice = np.mean(temperature_matrix_noice, axis=0)
mean_by_day_noice = np.mean(temperature_matrix_noice, axis=1)

x = ["City 1", "City 2", "City 3"]
y = mean_by_city_noice
plt.title("Average temperature by city during the week")
plt.xlabel("City")
plt.ylabel("Average temperature")
plt.bar(x, y)
plt.show()

print(f"Original temperature matrix (°C): \n{temperature_matrix}")
print(f"Average temperature for each city: {mean_by_city}")
print(f"Maximum Temperature for each day: {max_temp_by_day}")
print(f"Coldest day for each city: {min_temp_by_city}")
print(f"Temperature matrix with noise (°C): \n{temperature_matrix_noice}")
print(f"Average temperature with noise for each city: {mean_by_city_noice}")
print(f"Average temperature with noice for each day: {mean_by_day_noice}")