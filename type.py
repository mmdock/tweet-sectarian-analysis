##Determine if a given tweet is racist
##Input a single tweet (as given from streaming API or otherwise)
##Returns True/False if the given tweet is racist.

##Basically preporcesses a tweet and then checks the string against a set of known racist tweets.
##DCS

import re
import json
import nltk
nltk.download("stopwords")  # Download stop words, only needed once
from nltk.corpus import stopwords


def type(tweet):
    #A set of stopwords is created, filter out non context sensitive.
    stopwrd = set(stopwords.words("english"))
    #cleanup regex placeholders
    stopwrd.update({'UNAME'})
    stopwrd.update({'WEB'})
    #text cleanup
    tweet = convert(tweet)
    tweet = word_list(tweet,stopwrd)
    print(tweet)
    ##import "bad" word list and save it as a set(faster search").
    words = set(line.strip() for line in open('badwords.txt'))
    if any(word in tweet for word in words):
        return True
    return False

def convert(tweet):
    #lowercase conversion
    tweet = tweet.lower()
    #remove URL formating
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','WEB',tweet)
    #clean up whitespace
    tweet = re.sub('[\s]+', ' ', tweet)
    #cleanup hashtag data
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #cleanup usernames
    tweet = re.sub('@[^\s]+','UNAME',tweet)
    #remove non letters
    tweet = re.sub('[^a-zA-Z]', ' ' , tweet)
    tweet = replaceTwoOrMore(tweet)
    return tweet

def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)

def word_list(tweet, stopwrd):
    #split into individual words
    words = tweet.split()
    #Remove stop words
    words = [w for w in words if not w in stopwrd]
    return(" ".join(words))

type("Damn Niggers in the White House #burnemall @jojo")
