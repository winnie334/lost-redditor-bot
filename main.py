import praw, os, time, datetime, random, re
from praw.models import Comment


def log_in():
    print('Logging in...')
    bot = praw.Reddit(user_agent='LostRedditors by winnie33',
                    client_id='jiZMcG6Mc7-cNg',
                    client_secret='',
                    username='LostRedditorsBot',
                    password='')
    print("Logged in")
    return bot

def scan_and_respond(bot):
    newcomments = bot.subreddit('all').stream.comments()
    for comment in newcomments:
        if re.search("^(/r/|r/)", comment.body.lower()) and all(notAllowed not in comment.body.lower() for notAllowed in ["\n", " ", "?"]):
            print(comment.body.lower(), "- found in", comment.subreddit)
            referencedSub = comment.body.lower().replace("/r/", "").replace("r/", "")
            currentSub = str(comment.subreddit).lower()
            if (referencedSub == currentSub and all(forbiddenSub != currentSub for forbiddenSub in ["lostredditors", "whoosh"])):
                respond_to_comment(comment)

def respond_to_comment(comment):
    if (comment.author.name == "LostRedditorsBot"):
        print("almost replied to ourselves..")
        return
    print("responding to comment at https://www.reddit.com"+ comment.permalink)
    comment.reply("r/lostredditors")


if __name__ == "__main__":
    bot = log_in()
    scan_and_respond(bot)
