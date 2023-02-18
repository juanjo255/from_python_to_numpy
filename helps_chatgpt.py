# Sample temperature data in degrees Celsius
temperature_data = [-30, -20, 0, 10, 20, 40, 60, 80, 100, 110, 120, 130]

# Scale the data to a new range of 0 to 100 degrees Celsius
new_min = 0
new_max = 100
min_value = min(temperature_data)
max_value = max(temperature_data)
scaling_factor = (new_max - new_min) / (max_value - min_value)
print(scaling_factor)
scaled_data = [scaling_factor * (x - min_value) + new_min for x in temperature_data]
print(scaled_data)
import numpy as np 
import statistics
a = np.array(scaled_data)
print (statistics.stdev(a))
print(np.std(a))

