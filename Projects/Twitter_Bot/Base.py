# get info from reddit
# package info into a good format
# Post on twitter

#imports
import praw
import keyboard
import sys
sys.path.append(".")
from configs import reddit_config
import time
import os

# log in definition
#def bot_login():
reddit = praw.Reddit(username = reddit_config.username,
        password = reddit_config.password,
        client_id = reddit_config.client_id,
        client_secret = reddit_config.client_secret,
        user_agent = 'Joke stealer.')

for submission in reddit.subreddit("jokes").hot(limit=10):
    print(submission.title)
    print(submission.)
    print('')