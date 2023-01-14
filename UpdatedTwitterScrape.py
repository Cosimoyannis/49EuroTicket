import tweepy
import csv

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


csvFile = open('../../csv/dataset.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
#csvWriter.writerow(["Timestamp", "Tweet", "Hashtags", "Tweet_ID"])
counter = 0

for tweet in tweepy.Cursor(api.search_full_archive,
                            #label must be set account specific!
                            label= '',
                            query= '#wm2022 OR #wmkatar lang:de',
                            fromDate = "202101010000",
                            toDate = "202202260000"
                          ).items():
    status = api.get_status(tweet.id, tweet_mode="extended")
    if not tweet.retweeted and 'RT @' not in tweet.text:
        csvWriter.writerow([tweet.created_at, status.full_text, tweet.entities['hashtags'], tweet.id])
        counter += 1
        print(counter)