import json
import pandas as pd
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
import threading
from config import *
import os.path as path
from train.train import KNNClassifier

app = Flask(__name__, template_folder="web_serve/mytemplate")
app.config['GOOGLEMAPS_KEY'] = google_token_key
GoogleMaps(app, key=google_token_key)

def my_max(li):
    return max(li)

icons = ['//maps.google.com/mapfiles/ms/icons/blue-dot.png', '//maps.google.com/mapfiles/ms/icons/green-dot.png', icons.dots.yellow, icons.dots.red]
class Markers(object):
    class __Markers:
        def __init__(self):
            self.val = [None]
        def __str__(self):
            return ('self' + '\n'.join(self.val))
    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not Markers.instance:
            Markers.instance = Markers.__Markers()
        return Markers.instance
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)

@app.route("/")
def fullmap():
    m = Markers()
    fullmap = Map(
        identifier="fullmap",
        varname="fullmap",
        style=(
            "height:100%;"
            "width:100%;"
            "top:0;"
            "left:0;"
            "position:absolute;"
            "z-index:200;"
        ),
        lat=37.4419,
        lng=-122.1419,
        markers= m.val,
        zoom = "4",
    )
    return render_template('example_fullmap.html', fullmap=fullmap)

@app.route("/statistics")
def statistics():
    df = pd.read_csv("stats.csv", names=["", "author", "city", "state", "lat", "lng", "text"])
    labels = []
    values = []
    ## City
    labs = list(df.city.unique())
    vals = []
    for label in labs:
        vals.append((df[df.city == label]).shape[0])
    values.append(vals)
    labels.append(labs)

    ## Author
    labs = list(df.author.unique())
    vals = []
    for label in labs:
        vals.append((df[df.author == label]).shape[0])
    values.append(vals)
    labels.append(labs)

    ##States
    labs = list(df.state.unique())
    vals = []
    for label in labs:
        vals.append((df[df.state == label]).shape[0])
    values.append(vals)
    labels.append(labs)

##    ## City avg
##    labs = list(df.city.unique())
##    vals = []
##    for label in labs:
##        vals.append((df[df.city == label]).mean())
##    values.append(vals)
##    labels.append(labs)
##
##    ##States avg
##    labs = list(df.state.unique())
##    vals = []
##    for label in labs:
##        vals.append((df[df.state == label]).mean())
##    values.append(vals)
##    labels.append(labs)
##
##    ## Author avg
##    labs = list(df.author.unique())
##    vals = []
##    for label in labs:
##        vals.append((df[df.author == label]).mean())
##    values.append(vals)
##    labels.append(labs)
    return render_template('index.html', values=values, labels=labels)

class TweetStreamListener(StreamListener):

    def __init__(self):
        self.classifier = KNNClassifier('train/train.csv')

    # on success
    def on_data(self, data):
        # decode json
        dict_data = json.loads(data)
        if "text" not in dict_data:
            return
        if not dict_data.get("place"):
            return
        print(json.dumps(dict_data, indent=4, sort_keys=True))
        m = Markers()

        if not dict_data["user"]["location"]:
            c1 = dict_data["place"]["full_name"]
            c1 = c1.strip().split(", ")
        elif not dict_data["place"]["full_name"]:
            c1 = dict_data["place"]["full_name"]
            c1 = c1.strip().split(", ")
        else:
            c1 = ["NA","NA"]

        author = [dict_data["user"]["screen_name"]]
        city = [c1[0]]
        state = [c1[1]]
        lng = [(dict_data["place"]["bounding_box"]["coordinates"][0][0][0] + dict_data["place"]["bounding_box"]["coordinates"][0][1][0] + dict_data["place"]["bounding_box"]["coordinates"][0][2][0] + dict_data["place"]["bounding_box"]["coordinates"][0][3][0])/4]
        lat = [(dict_data["place"]["bounding_box"]["coordinates"][0][0][1] + dict_data["place"]["bounding_box"]["coordinates"][0][1][1] + dict_data["place"]["bounding_box"]["coordinates"][0][2][1] + dict_data["place"]["bounding_box"]["coordinates"][0][3][1])/4]
        text = [(dict_data["text"])]

        if(dict_data["place"]["country_code"] == "US"):
            sentiment = self.classifier.classify(dict_data['text'], KNNClassifier.SENTIMENT)
            category = self.classifier.classify(dict_data['text'], KNNClassifier.CATEGORY)

            m.val.append({'icon': icons[0], 'lng': lng, 'lat': lat, 'infobox': text})
            d = {'author': author, 'city': city, 'state':state, 'lat':lat, 'lng': lng, 'text': text, 'sentiment': sentiment, 'category': category}
            df = pd.DataFrame(data=d, columns=["author", "city", "state", "lat", "lng", "text", "sentiment", "category"])
            with open('stats.csv', 'a') as f:
                if not path.exists("stats.csv"):
                    df.to_csv(f, header = True)
                else:
                    df.to_csv(f, header = False)

        return True

    # on failure
    def on_error(self, status):
        print (status)

def begin_stream():

    # create instance of the tweepy tweet stream listener
    listener = TweetStreamListener()

    # set twitter keys/tokens
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Keywords for tracking:
    keywords = [line.strip() for line in open('keywords.txt')]
    # create instance of the tweepy stream
    stream = Stream(auth, listener)

    stream.filter(track=keywords, languages = ['en'])

if __name__ == '__main__':

    # search twitter for "congress" keyword
  #  threading.Thread(target=begin_stream).start()
    app.run(debug=True, use_reloader=True, host= '0.0.0.0')
