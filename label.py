##Labler, reads in a csv of tweets. text displays so that we can manully label text.
##Outputs labled tweets to a csv that we can combine later and feed to a model.

##DCS

import pandas as pd
import sys

def label(tweets):
    with open(tweets) as f:
        content = f.readlines()
    try:
        group = str(input("Select data set, 1, 2, or 3.: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
    if  (group == "1"):
        lab(0,5,content)
    elif(group == "2"):
        lab(500,1000,content)
    elif(group == "3"):
        lab(1001,1500,content)
    else:
        print("Invalid Entry")

def lab(start, stop,content):
    ratings = []
    texts = []
    types = []
    rated = 0
    for x in range(start, stop):
        print("You Have Rated... " + str(rated) + "\n")
        if(rated == 251):
            break
        print(content[x] + "\n")
        while True:
            try:
                type = str(input("Select Type: 7=Other 6=Political, 5= Disability, 4=sexual orientation, 3=racial, 2=gender, 1=religion, 0=skip "))
                #skip
                if(type == "0"):
                    break
                rating = str(input("Select Sentiment. 5= Pro Racist, 1=Anti Racist: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            #Pro Racist Remarks
            if(rating == "5"):
                texts.append(content[x])
                ratings.append('5')
                types.append(type)
                rated +=1
                break
            #Anti racist remark
            elif(rating == "1"):
                texts.append(content[x])
                ratings.append('1')
                types.append(type)
                rated +=1
                break
            else:
                print("Invalid Entry")
                print(content[x])
                continue
    d = {'text': texts, 'sentiment': ratings, 'types':types}
    df = pd.DataFrame(data=d)
    df.to_csv('ratingout.csv')

label("raw_tweets.txt")
