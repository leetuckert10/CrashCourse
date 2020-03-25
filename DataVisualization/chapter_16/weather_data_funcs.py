# Miscellaneous functions for processing weather data.

import csv
from typing import List, Any


def get_header_info(filename: str):
    try:
        with open(filename, 'r') as f:
            reader: Any = csv.reader(f)
            header_row: List[str] = next(reader)  # read the first line
            for index, column_header in enumerate(header_row):
                print(index, column_header)
    except FileNotFoundError:
        print(f"Cannot open {filename}!")
        exit(1)


filename: str = 'data/sitka_weather_2018_simple.csv'
get_header_info(filename)
