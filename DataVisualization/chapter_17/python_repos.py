# python_repos.py
#
# Experimenting with pulling data from a web API.

import requests
from typing import Dict, List


def get_data() -> requests.models.Response:
    # Make an API call and store the results.
    url: str = 'https://api.github.com/search/repositories?q=language:python' \
               '&sort=stars'
    headers: Dict = {'Accept': 'application/vnd.github.v3+jason'}
    r: requests.models.Response = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")
    return r


def get_dicts(r: requests.models.Response) -> List:
    # Store API response in a variable.
    response_dict: Dict = r.json()
    print(f"Total repositories: {response_dict.get('total_count')}")
    repo_dicts: List = response_dict.get('items')
    print(f"Repositories returned: {len(repo_dicts)}")
    return repo_dicts


def print_data(repo_dicts: List) -> None:
    # Process results.
    print("\nSelected information about the first repository:")
    for repo_dict in repo_dicts:
        print(f"Name: {repo_dict.get('name')}")
        print(f"Owner: {repo_dict.get('owner').get('login')}")
        print(f"Stars: {repo_dict.get('stargazers_count')}")
        print(f"Repository: {repo_dict.get('html_url')}")
        print(f"Created: {repo_dict.get('created_at')}")
        print(f"Updated: {repo_dict.get('updated_at')}")
        print(f"Description: {repo_dict.get('description')}\n")


if __name__ == '__main__':
    res = get_data()
    dict_list: List = get_dicts(res)
    print_data(dict_list)
