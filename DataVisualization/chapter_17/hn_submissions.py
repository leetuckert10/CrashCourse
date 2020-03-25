# hn_submissions.py

import requests
from typing import List, Dict
from operator import itemgetter


# This API call returns a list containing the ID's of up to 500 top stories.
url: str = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids: List = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate call for each submission and capture the data we need.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"Id: {submission_id}\tStatus: {r.status_code}")
    response_dict: Dict = r.json()
    # Build a dictionary for each submission to capture the data we need.
    url = url.split('.')[0]
    submission_dict = {
        'title': response_dict.get('title'),
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants'),
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict.get('title')}")
    print(f"Discussion link: {submission_dict.get('hn_link')}")
    print(f"Comments: {submission_dict.get('comments')}")


