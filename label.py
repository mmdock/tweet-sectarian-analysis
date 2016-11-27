##Labler, reads in a csv of tweets. text displays so that we can manully label text.
##Outputs labled tweets to a csv that we can combine later and feed to a model.

##DCS

import pandas as pd
import sys

def label(tweets):
    ratings = []
    data = pd.read_csv(tweets)
    for index, row in data.iterrows():
        print(row['text'])
        while True:
            try:
                rating = str(input("Select Sentiment 5=Pro Racism, 1=Against Racism: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue

            if  (rating == "5"):
                ratings.append('5')
                break
            elif(rating == "1"):
                ratings.append('1')
                break
            else:
                print("Invalid Entry")
                print(row['text'])
                continue
    data['sentiment'] = ratings
    data.to_csv('out.csv')

label("tweets.csv")
