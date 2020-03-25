# high_low_temps.py
# Per exercise 16-4, this script operates on a generic set of temperature
# data as downloaded from NOAA Climate Data Online.

import csv
import matplotlib.pyplot as plt     # type: ignore
from typing import List, Any
from datetime import datetime


def get_user_input() -> str:
    """Get a CSV file name for parsing weather data."""
    print("Enter the name of a CSV file of weather data to parse.")
    file_name = input("File name including path if necessary: ")
    return file_name


highs: List[int] = []
lows: List[int] = []
dates: List[str] = []
header_row: List[str]
name_index: int
tmin_index: int
tmax_index: int

filename: str = get_user_input()
try:
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header_row = next(reader)               # read the first line
        try:
            name_index = header_row.index("NAME")
            tmin_index = int(header_row.index("TMIN"))
            tmax_index = int(header_row.index("TMAX"))
        except ValueError:
            print(f"{filename} is not formatted per program specifications.")
            exit(0)
        else:
            for row in reader:
                try:
                    high: int = int(row[tmax_index])
                    low: int = int(row[tmin_index])
                    date_s: Any = datetime.strptime(row[2], '%Y-%m-%d').date()
                    location: str = row[name_index]
                except ValueError:
                    print(f"No data for {date_s}...")
                else:
                    highs.append(high)
                    lows.append(low)
                    dates.append(date_s)
                    location_name: str = location
except FileNotFoundError:
    print(f"Cannot open {filename}!")
    exit(1)

# Plot the high temperatures.
# Set the plot style.
plt.style.use("seaborn")
fig, ax = plt.subplots(figsize=(9, 10))

# Display high temperatures in red.
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format the plot.
date_range: str = f"{dates[0]} through {dates[-1]}"
plt.title(f"Daily high and low temperatures - {date_range}\n{location_name}",
          fontsize=14)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.yticks(range(0, 140, 10))
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
