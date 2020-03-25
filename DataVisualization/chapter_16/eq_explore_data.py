# eq_explore_data.py

import json
from typing import Any, Dict, List


def write_readable_file(file: str, all_eq_data: Any):
    """Write a json file into a readable format using json.dump()"""
    with open(file, 'w') as f:
        json.dump(all_eq_data, f, indent=4)


def load_json_data_from_file(file: str) -> Any:
    """Load data from a json file with json.load()."""
    with open(file) as f:
        all_eq_data: Any = json.load(f)
        return all_eq_data


filename: str = 'data/eq_data_1_day_m1.json'
json_load: Any = load_json_data_from_file(filename)

#readable_file: str = 'data/readable_eq_data.json'
#write_readable_file(readable_file, json_load)

mags: List = []
lons: List = []
lats: List = []
all_eq_dicts: List = json_load['features']
for eq_dict in all_eq_dicts:
#   print(f"magnitude: {eq_dict['properties']['mag']}")
    mags.append(eq_dict.get('properties').get('mag'))
    lons.append(eq_dict.get('geometry').get('coordinates')[0])
    lats.append(eq_dict.get('geometry').get('coordinates')[1])

print(mags)
print(lons)
print(lats)
