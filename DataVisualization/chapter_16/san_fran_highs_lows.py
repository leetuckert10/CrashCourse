# sitka_highs_lows.py

import csv
import matplotlib.pyplot as plt     # type: ignore
from typing import List, Any
from datetime import datetime
from datetime import date

highs: List[int] = []
lows: List[int] = []
dates: List[str] = []

filename: str = "data/san_francisco_2019.csv"
try:
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header_row: List[str] = next(reader)          # read the first line
        name_index: int = header_row.index("NAME")
        tmin_index: int = int(header_row.index("TMIN"))
        tmax_index: int = int(header_row.index("TMAX"))

        print(f"TMIN: {tmin_index}, TMAX: {tmax_index}")
        for row in reader:
            highs.append(int(row[tmax_index]))
            lows.append(int(row[tmin_index]))
            date_str: Any = datetime.strptime(row[2], '%Y-%m-%d').date()
            dates.append(date_str)
            location_name: str = row[name_index]
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
date_range: str = f"{dates[1]} through {dates[-1]}"
plt.title(f"Daily high and low temperatures - {date_range}\n{location_name}",
          fontsize=14)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.yticks(range(30, 140, 10))
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
