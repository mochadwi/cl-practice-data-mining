import tweepy
from tweepy.auth import OAuthHandler
import config
import json
 
auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)
 
api = tweepy.API(auth)

def store_tweet(tweet):
    print(tweet)

for status in tweepy.Cursor(api.user_timeline).items(10):
    # Process a single status
    store_tweet(status.text)