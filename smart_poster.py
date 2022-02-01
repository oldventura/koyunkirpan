#!/usr/bin/python3
#-*- encoding:utf-8 -*-

from __future__ import unicode_literals
import os
import json
import praw
import secrets
import warnings

warnings.filterwarnings('ignore')

reddit = praw.Reddit(
  "koyunkirpan",
  config_interpolation = "basic"
)

## MAIN CLASS
class runner:
  def __init__(self):
    self.posts              = []
    self.posted_on          = []
    self.subreddits         = ['oddlysatisfying', 'nextfuckinglevel', 'interestingasfuck', 'WatchPeopleDieInside', 'BeAmazed', 'blackmagicfuckery', 'Damnthatsinteresting', 'PublicFreakout']
    self.subreddit          = reddit.subreddit(self.subreddits[secrets.randbelow(len(self.subreddits))])
    self.path               = os.getcwd()
    self.search_limit       = 20
    self.post_limit         = 50

  def load_posted_on(self):
    with open(os.path.join(self.path, 'smart_poster_savedata.json'),) as f:
      self.posted_on = json.load(f)

  def find_posts(self):
    for submission in self.subreddit.top("week", limit=self.post_limit):
      if submission.id not in self.posted_on['ids']:
        self.posts.append(submission)

  def post_random(self):
    selected_post = self.posts[secrets.randbelow(len(self.posts))]
    title         = os.popen('trans -b -t tr "%s"' %(selected_post.title)).read().strip()
    print("Title:", title)
    print("URL:", 'https://www.reddit.com'+selected_post.permalink+"\n")

    selected_post.crosspost(subreddit="KGBTR", title=title, nsfw=selected_post.over_18)

    self.posted_on['ids'].append(selected_post.id)
    with open(os.path.join(self.path, 'smart_poster_savedata.json'), 'w') as json_file:
      json.dump(self.posted_on, json_file, indent=4, sort_keys=True)

if __name__ == '__main__':
  x = runner()
  print ("Starting new crosspost run...\n")
  x = runner()
  x.load_posted_on()
  x.find_posts()
  x.post_random()
  print("done.")
