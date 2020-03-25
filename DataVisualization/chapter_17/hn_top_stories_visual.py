# Exercise 17-2: hn_submissions.py
# Using the data from hn_submissions.py, make a bar chart showing the most
# active discussions currently happening on Hacker News.
#
# This program fixes two issues from the example in the Crash Course book. It
# handles a situation where number of comments is None instead of zero. A
# value of None breaks the sorted() function.
#
# Also, the original example was just getting the first 30 articles and then
# sorting that by number of comments. That is not truly the top 30 stories.
# This version fixes that. Also, I took this stuff and put in in a class
# called HNTopStories.

import requests
from plotly import offline              # type: ignore
from typing import List, Dict, Any
from operator import itemgetter


class HNTopStories:
    """This class encapsulates the functionality required to pull the top 30
    discussions from Hacker's News and display them on a bar chart sorted by
    the articles number of discussions."""
    def __init__(self):
        """Initialize class data."""
        # This API call returns a list containing the ID's of up to 500 top
        # stories.
        self.url: str = 'https://hacker-news.firebaseio.com/v0/topstories.json'
        self.submission_dicts: List = []
        self.r = None       # cannot figure out how to annotate this
        self.top_30: Dict = {}

    def get_data(self):
        """This method gets the data which consists of a list of submission
        Id's."""
        self.r = requests.get(self.url)
        print(f"Status code: {self.r.status_code}")

    def process_data(self):
        """This method accumulates the data required to generate the chart
        and build a link to the comments section of each article."""
        # Process information about each submission.
        submission_ids: List = self.r.json()
        for submission_id in submission_ids:
            # Make a separate call for each submission and capture the data
            # we need.
            url: str = f"https://hacker-news.firebaseio.com/v0/item/" \
                  f"{submission_id}.json"
            self.r = requests.get(url)
            response_dict: Dict = self.r.json()
            # Build a dictionary for each submission to capture the data we
            # need.
            long_title: str = response_dict.get('title')
            title: str = (long_title[:30] + '...') if len(long_title) > 33 else\
                long_title
            submission_dict: Dict = {
                'title': title,
                'hn_link': f"<a href='https://news.ycombinator.com/item?id="
                           f"{submission_id}'>{title}</a>",
                'comments': response_dict.get('descendants'),
                'submission_id': submission_id,
                'author': response_dict.get('by'),
                'labels': f"{response_dict.get('by')}<br />{long_title}",
            }
            # Handle where the value for comments, which is supposed to be a
            # number, is None. A value on None breaks the sorted() function.
            if submission_dict.get('comments') is None:
                submission_dict['comments'] = 0

            self.submission_dicts.append(submission_dict)

        # Sort the dictionary data by number of comments.
        self.submission_dicts = sorted(self.submission_dicts, key=itemgetter(
            'comments'), reverse=True)
        # We only want the top 30.
        self.top_30 = self.submission_dicts[:30]

    def print_data(self):
        """This is a utility method that simply displays some of the meaningful
        data."""
        for submission_dict in self.submission_dicts:
            print(f"\nAuthor: {submission_dict.get('author')}")
            print(f"Title: {submission_dict.get('title')}")
            print(f"Discussion link: {submission_dict.get('hn_link')}")
            print(f"Comments: {submission_dict.get('comments')}")

    def visualize(self):
        """This method create the visualization."""
        num: List[str] = [num['comments'] for num in self.top_30]
        links: List[str] = [links['hn_link'] for links in self.top_30]
        labels: List[str] = [label['labels'] for label in self.top_30]
        # Make the visualization.
        data: List[Dict] = [{
            'type': 'bar',
            'x': links,
            'y': num,
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

        # We don't use the Layout class because we are using the dictionary
        # method to
        # define the layout.
        my_layout: Dict[str, Any] = {
            'title': 'Top 30 Active Discussions on Hacker News',
            'titlefont': {'size': 28},
            'xaxis': {
                'title': 'Article Title and Link',
                'titlefont': {'size': 24},
                'tickfont': {'size': 14},
            },
            'yaxis': {
                'title': 'Number Comments',
                'titlefont': {'size': 24},
                'tickfont': {'size': 14},
            },
        }

        fig: Dict = {
            'data': data,
            'layout': my_layout
        }
        offline.plot(fig, filename='top_hn_stories.html')


hn_top_stories = HNTopStories()
hn_top_stories.get_data()
hn_top_stories.process_data()
#hn_top_stories.print_data()
hn_top_stories.visualize()
