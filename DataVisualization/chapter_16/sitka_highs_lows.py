# sitka_highs_lows.py

import csv
import matplotlib.pyplot as plt     # type: ignore
from typing import List, Any
from datetime import datetime

highs: List[int] = []
lows: List[int] = []
dates: List[str] = []

filename: str = "data/sitka_weather_2018_simple.csv"
try:
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header_row: List[str] = next(reader)          # read the first line

        for row in reader:
            highs.append(int(row[5]))
            lows.append(int(row[6]))
            date_str: Any = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(date_str)
except FileNotFoundError:
    print(f"Cannot open {filename}!")
    exit(1)

# Plot the high temperatures.
# Set the plot style.
plt.style.use("seaborn")
fig, ax = plt.subplots(figsize=(9, 9))

# Display high temperatures in red.
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format the plot.
plt.title("Daily high and low temperatures - 2018\nSitka, AK", fontsize=14)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.yticks(range(30, 140, 10))
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
