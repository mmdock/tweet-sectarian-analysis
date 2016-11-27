from flask import Flask, render_template
from jinja2 import Template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

import tweepy
from config import *
app = Flask(__name__, template_folder="mytemplate")

@app.route('/')
def index():
    return render_template('index.html', names="John")


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.user_timeline(id='california')

@app.route('/twitter')
def twitterdisplayer():
    tweets_text = []
    for tweet in public_tweets:
        tweets_text.append(tweet.text)
    return "\n\n".join(tweets_text)

if(__name__) == '__main__':
    app.run(debug=True)
