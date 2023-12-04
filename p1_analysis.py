import json
import matplotlib.pyplot as plt
from datetime import datetime

#Getting api file
with open('api_data_test.json', 'r') as file:
    data = json.load(file)
# empty lists to append JSON entries
factors = []
times = []

for timestamp, entry in data.items():
    factors.append(entry["factor"])
    times.append(datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"))

##### Plot looking at the relationship between "factor" and "time"; if any
plt.plot(times, factors, marker='o', linestyle='-', color='b')
plt.title('Factor vs. Time')
plt.xlabel('Time')
plt.ylabel('Factor')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

##### Plot looking at the relationship between "pi" and "time"; if any
# empty list to put JSON pi data into
pi_value = []
time = []

for timestamp, entry in data.items():
    pi_value.append(entry["pi"])
    time.append(datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"))

# Plotting pi vs. time
plt.plot(time, pi_value, marker='o', linestyle='-', color='r')
plt.title('Pi Value vs. Time')
plt.xlabel('Time')
plt.ylabel('Pi Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

##### Plot looking at the relationship between "pi" and "factor"; if any
# empty list to put JSON pi data into
pi = []
factor_1 = []

for timestamp, entry in data.items():
    pi.append(entry["pi"])
    factor_1.append(entry["factor"])
plt.plot(factor_1, pi, marker='o', linestyle='-', color='c')
plt.title('Pi Value vs. Factor')
plt.xlabel('Factor')
plt.ylabel('Pi Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()