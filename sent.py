import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch
import time
import io
# import twitter keys and tokens
from config import *

# create instance of elasticsearch
es = Elasticsearch()


class TweetStreamListener(StreamListener):

    def __init__(self, start_time, time_limit=60):
        self.time = start_time
        self.limit = time_limit
        self.tweet_data = []
        
    # on success
    def on_data(self, data):
 
        saveFile = io.open('raw_tweets.json', 'a', encoding='utf-8')
        while (time.time() - self.time) < self.limit:
            try:
                dict_data = json.loads(data)
                self.tweet_data.append(dict_data["text"])
                return True
            except BaseException:
                print ('failed ondata,', str(e))
                time.sleep(5)
                pass
 
        saveFile = io.open('raw_tweets.csv', 'w', encoding='utf-8')
        saveFile.write(u'[\n')
        saveFile.write(','.join(self.tweet_data))
        saveFile.write(u'\n]')
        saveFile.close()
        exit()
##    def on_data(self, data):
##
##        # decode json
##        dict_data = json.loads(data)
##        # pass tweet into TextBlob
##        if "text" not in dict_data:
##            return
##        if not dict_data.get("place"):
##            return
##        tweet = TextBlob(dict_data["text"])
##        print(json.dumps(dict_data, indent=4, sort_keys=True))
##        # determine if sentiment is positive, negative, or neutral
##        if tweet.sentiment.polarity < 0:
##            sentiment = "negative"
##        elif tweet.sentiment.polarity == 0:
##            sentiment = "neutral"
##        else:
##            sentiment = "positive"
##
##        # output sentiment
##        print (str(tweet.sentiment.polarity) + " " + sentiment)
##
##        # add text and sentiment info to elasticsearch
##        es.index(index="sentiment",
##                 doc_type="test-type",
##                 body={"author": dict_data["user"]["screen_name"],
##                       "date": dict_data["created_at"],
##                       "location": dict_data["user"]["location"],
##                       "message": dict_data["text"],
##                       "polarity": tweet.sentiment.polarity,
##                       "subjectivity": tweet.sentiment.subjectivity,
##                       "sentiment": sentiment,
##                       "timestamp": dict_data["timestamp_ms"],
##                       "place": dict_data["place"]["full_name"]}
##                 )
##        return True

    # on failure
    def on_error(self, status):
        print (status)

if __name__ == '__main__':

    # create instance of the tweepy tweet stream listener
    listener = TweetStreamListener(time.time(), time_limit=60)

    # set twitter keys/tokens
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Keywords for tracking:
    keywords = [line.strip() for line in open('badwords.txt')]
    # create instance of the tweepy stream
    start_time = time.time()
    stream = Stream(auth, listener)

    # search twitter for "congress" keyword
    stream.filter(track=keywords, languages = ['en'])
