# map_active_fire_data
# Using the data processing work from the first part of this chapter and the
# mapping work from this section, make a map that shows which parts of the
# world are affected by fires.

import csv
from datetime import datetime
from typing import Any, Dict, List
from plotly.graph_objects import Layout     # type: ignore
from plotly import offline                  # type: ignore


lons: List = []
lats: List = []
brightness: List = []

filename: str = 'data/MODIS_C6_Global_48h.csv'
try:
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)           # read the first line

        try:
            lat_idx: int = int(header.index("latitude"))
            lon_idx: int = int(header.index("longitude"))
            brightness_idx: int = int(header.index("brightness"))
            date_idx: int = int(header.index('acq_date'))
        except ValueError:
            print(f"{filename} is not formatted per program specifications.")
            exit(0)
        else:
            for row in reader:
                try:
                    lat = row[lat_idx]
                    lon = row[lon_idx]
                    bright = float(row[brightness_idx])
                    date_s: Any = datetime.strptime(row[date_idx],
                                                    '%Y-%m-%d').date()
                except ValueError:
                    print(f"No data for {date_s}...")
                else:
                    lats.append(lat)
                    lons.append(lon)
                    brightness.append(bright)
except FileNotFoundError:
    print(f"Cannot open {filename}!")
    exit(1)

data: List = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
#   'text': txts,
    'marker': {
        'size': 4,
        'color': brightness,
        'colorscale': 'Reds',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    },
}]
my_layout = Layout(title="Active Fires Worldwide")
# Create a dictionary called fig that contains the data and the layout to be
# passed along to offline.plot().
fig: Dict = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_active_fires.html')
