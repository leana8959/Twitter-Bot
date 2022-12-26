import os
from twitter_bot_class import Twitter_Bot
import argparse

"""
Likes tweets based on the keywords you entered
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Like tweets associated to a keyword")
    parser.add_argument("--username", type=str, help="Username of your account")
    parser.add_argument("--password", type=str, help="Password of your account")
    parser.add_argument("--keyword", type=str, help="Keyword of your choice")
    args = parser.parse_args().__dict__
    USERNAME = args['username']
    PASSWORD = args['password']
    KEYWORD = args['keyword']

    try:
        tbot = Twitter_Bot(USERNAME, PASSWORD)
        tbot.login()
        tbot.search(KEYWORD)
        tbot.like_tweets(10)
        tbot.logout()
    except Exception as e:
        tbot.logout()
        print(e)
