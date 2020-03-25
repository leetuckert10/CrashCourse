# boon_weather_data.py

import csv
import matplotlib.pyplot as plt     # type: ignore
from typing import List, Any
from datetime import datetime

highs: List[int] = []
lows: List[int] = []
dates: List[str] = []

filename: str = "data/grandfather_mountain_weather_2019.csv"
try:
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header_row: List[str] = next(reader)          # read the first line

        for row in reader:
            date_str: Any = datetime.strptime(row[2], '%Y-%m-%d')
            try:
                high: int = int(row[8])
                low: int = int(row[9])
            except ValueError:
                print(f"Missing data for {date_str}.")
            else:
                highs.append(high)
                lows.append(low)
                dates.append(date_str)
except FileNotFoundError:
    print(f"Cannot open {filename}!")
    exit(1)

# Plot the high temperatures.
# Set the plot style.
plt.style.use("seaborn")
fig, ax = plt.subplots()

# Display high temperatures in red.
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format the plot.
plt.title("Daily high and low temperatures - 2019\nGrandfather Mountain, NC",
          fontsize=14)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
