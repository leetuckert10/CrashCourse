# eq_explore_data.py

import json
from typing import Any, Dict, List
from plotly.graph_objects import Layout     # type: ignore
from plotly import offline                  # type: ignore


def write_readable_file(file: str, all_eq_data: Any):
    """Write a json file into a readable format using json.dump()"""
    with open(file, 'w') as f:
        json.dump(all_eq_data, f, indent=4)


def load_json_data_from_file(file: str) -> Any:
    """Load data from a json file with json.load()."""
    with open(file) as f:
        all_eq_data: Any = json.load(f)
        return all_eq_data


filename: str = 'data/1.0_month.geojson.json'
json_load: Any = load_json_data_from_file(filename)

#readable_file: str = 'data/readable_eq_data.json'
#write_readable_file(readable_file, json_load)

mags: List = []
lons: List = []
lats: List = []
txts: List = []
title: str = json_load.get('metadata').get('title')
all_eq_dicts: List = json_load['features']
for eq_dict in all_eq_dicts:
#   print(f"magnitude: {eq_dict['properties']['mag']}")
    mags.append(eq_dict.get('properties').get('mag'))
    lons.append(eq_dict.get('geometry').get('coordinates')[0])
    lats.append(eq_dict.get('geometry').get('coordinates')[1])
    txts.append(eq_dict.get('properties').get('title'))

# Map the earthquakes.
#
# This is the simplest ways to define data for a chart in Plotly; however,
# it doesn't accommodate customization as is often required.
# data: List = [Scattergeo(lon=lons, lat=lats)]

data: List = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': txts,
    'marker': {
        'size': [mag*5 for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title=title)
# Create a dictionary called fig that contains the data and the layout to be
# passed along to offline.plot().
fig: Dict = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
