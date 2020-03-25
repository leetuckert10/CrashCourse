# Exercise 17-1: perl_repos_visual.py
#
# Create a visualization using data from the GitHub API which consists of all
# the active Python projects. Using the popularity data, map each project to
# a bar chard showing its popularity.
#
# I am unable to establish annotations for some of these variables.

import requests
from plotly.graph_objects import Bar    # type: ignore
from plotly import offline              # type: ignore
from typing import Dict, List, Any


# Make an API call to GitHub searching for projects where the language is
# Python and sort by number of stars.
url: str = 'https://api.github.com/search/repositories?q=language:perl' \
           '&sort=stars'
# Define headers that explicitly ask for version 3 of the API. Is this
# necessary?
headers: Dict = {'Accept': 'application/vnd.github.v3+jason'}
# This returns a Response object but I don't know how to annotate the 'r'
# variable.
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable of type Dict.
response_dict: Dict = r.json()
print(f"Total repositories: {response_dict.get('total_count')}")

# Cannot get the annotation right on the rep_dicts_list variable.
repo_dicts_list: List[Any] = response_dict.get('items')

# Gather the data and store in two lists.
repo_links: List[str] = []
labels: List[str] = []
stars: List[int] = []
for repo_dict in repo_dicts_list:
    repo_name: str = repo_dict.get('name')
    repo_url: str = repo_dict.get('url')
    stars.append(repo_dict.get('stargazers_count'))
    owner: str = repo_dict.get('owner').get('login')
    description: str = repo_dict.get('description')
    labels.append(f"{owner}<br />{description}")
    # HTML anchor tag
    repo_links.append(f"<a href='{repo_url}'>{repo_name}</a>")

# Make the visualization.
data: List[Dict] = [{
        'type': 'bar',
        'x': repo_links,
        'y': stars,
        'hovertext': labels,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {
                'width': 1.5,
                'color': 'rgb(25,25,25)'
            },
        },
        'opacity': 0.6,
}]

# We don't use the Layout class because we are using the dictionary method to
# define the layout.
my_layout: Dict[str, Any] = {
    'title': 'Perl Projects on GitHub Sorted by Popularity',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig: Dict = {
    'data': data,
    'layout': my_layout
}
offline.plot(fig, filename='python_repos.html')
