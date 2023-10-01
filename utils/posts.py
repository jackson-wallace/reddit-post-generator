import praw
from config import PRAW_CLIENT_ID, PRAW_CLIENT_SECRET, PRAW_USER_AGENT

# PRAW setup
reddit = praw.Reddit(
    client_id=PRAW_CLIENT_ID,
    client_secret=PRAW_CLIENT_SECRET,
    user_agent=PRAW_USER_AGENT,
)


def get_posts(subreddit_name, post_count=11):
    subreddit = reddit.subreddit(subreddit_name)
    return [post for post in subreddit.hot(limit=post_count)]
