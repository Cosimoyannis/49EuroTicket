import tweepy
import configparser
import pandas as pd
from datetime import datetime


# FUNKTIONIERT !

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


date_since_pro = "202008130000"

hastag = '49euroticket'
limit=10


tweets=tweepy.Cursor(api.search_full_archive, query=hastag, fromDate=date_since_pro, label='49euroticket').items(limit)

columns = ['User', 'Time', 'Tweet', 'Likes']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.created_at, tweet.text, tweet.favorite_count])

df = pd.DataFrame(data, columns=columns)

df.to_csv("49euroticketzwei.csv")

print(df)
