import praw, os, time, datetime, random, re
from praw.models import Comment



print('Logging in...')
bot = praw.Reddit(user_agent='LostRedditors by winnie33',
                client_id='jiZMcG6Mc7-cNg',
                client_secret='',
                username='LostRedditorsBot',
                password='')

newcomments = bot.subreddit('all').stream.comments()
for comment in newcomments:
    if re.search("^(/r/|r/)", comment.body.lower()) and all(notAllowed not in comment.body.lower() for notAllowed in ["\n", " "]):
        print(comment.body.lower(), "- found in", comment.subreddit)
        if (comment.body.lower().replace("/r/", "").replace("/r", "") == comment.subreddit):
            print("Lostredditor found? at https://www.reddit.com"+ comment.permalink)
