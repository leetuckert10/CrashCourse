# boon_weather_data.py

import csv
import matplotlib.pyplot as plt     # type: ignore
from typing import List, Any
from datetime import datetime

rainfall: List[float] = []
dates: List[str] = []

filename: str = "data/death_valley_2018_simple.csv"
try:
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header_row: List[str] = next(reader)          # read the first line

        for row in reader:
            date_str: Any = datetime.strptime(row[2], '%Y-%m-%d')
            try:
                rain: float = float(row[3])
            except ValueError:
                print(f"Missing data for {date_str}.")
            else:
                rainfall.append(rain)
                dates.append(date_str)
except FileNotFoundError:
    print(f"Cannot open {filename}!")
    exit(1)

# Plot the high temperatures.
# Set the plot style.
plt.style.use("seaborn")
fig, ax = plt.subplots()

# Display high temperatures in red.
ax.plot(dates, rainfall, c='blue', alpha=0.5)

# Format the plot.
plt.title("Daily rain fall - 2018\nDeath Valley, CA",
          fontsize=14)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
