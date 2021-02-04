import time
import random
import tweepy
from tweepy import api

API_KEY = "cA5q5WNUmtF7S5GTVGRIT9TC0"
API_SECRET_KEY = "yKVT9sV1pvKe8MgRWiw4L3c1C0ipVp3QVkkZp9CPBhZPcDrVIT"
ACCESS_TOKEN = "1343829111479828480-xVZF3SwW8cNrbxUPqDvO02y3QPYHKX"
ACCESS_SECRET_TOKEN = "JqOm8wX4uEPtvQimnouok66xFEte5sjDAqUc5JLA0K5EM"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

art_accounts = ["aic_african", "mia_japankorea", "cezanneart", "SovietArtBot"]


def retweeter():
    userId = random.choice(art_accounts)
    for tweet in tweepy.Cursor(api.user_timeline, id=userId).items():
        try:
            if not tweet.retweeted:
                tweet.retweet()
                print(f"Retweeted {userId}'s tweet")
                userId = random.choice(art_accounts)

            time.sleep(5)

        except Exception as e:
            print("Error!", e)
            pass


def follower():
    print("retrieving and following follwers...")
    for follower in tweepy.Cursor(api.followers).items():
        try:
            if not follower.following:
                api.create_friendship(follower.id)
                print(f"{follower.screen_name} was follwed back!")
        except Exception as e:
            print("error occured", e)
            pass


def like_retweeter():
    print("retrieving tweets...")
    mentions = tweepy.Cursor(api.mentions_timeline, tweet_mode="extended").items()
    for mention in mentions:
        if mention.user.id == api.me().id:
            return
        if not mention.favorited:
            try:
                mention.favorite()
                print(f"liked {mention.user.screen_name}'s tweet mentioning you")
            except Exception as e:
                print("error!", e)
                pass
        if not mention.retweeted:
            try:
                mention.retweet()
                print(f"retweeted {mention.user.screen_name}'s tweet mentioning you")
            except Exception as e:
                print("error!", e)
                pass


follower()
like_retweeter()
retweeter()
