##Labler, reads in a csv of tweets. text displays so that we can manully label text.
##Outputs labled tweets to a csv that we can combine later and feed to a model.

##DCS

import pandas as pd
import sys

def label(tweets):
    with open(tweets) as f:
        content = f.readlines()
    #split our labeling task
    try:
        group = str(input("Select data set, 1, 2, 3, or (0 for all): "))
    except ValueError:
        print("Sorry, I didn't understand that.")
    if  (group == "1"):
        lab(0,499,content)
    elif(group == "2"):
        lab(500,1000,content)
    elif(group == "3"):
        lab(1001,1500,content)
    elif(group == "0"):
        lab(0, len(content), content)
    else:
        print("Invalid Entry")

def lab(start, stop, content):
    rated = 0
    #loop thorugh the users range
    for x in range(start, stop):
        ratings = []
        texts = []
        types = []
        print("You Have Rated... " + str(rated) + "\n")
        print(content[x] + "\n")
        while True:
            #select the type and sentiment.
            try:
                type = str(input("Select Type: 7=Other 6=Political, 5= Disability, 4=sexual orientation, 3=racial, 2=gender, 1=religion, 0=skip "))
                #skip
                if(type == "0"):
                    break
                rating = str(input("Select Sentiment. 5= Pro Racist, 1=Anti Racist: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            #store appropriately.
            #Pro Racist Remarks
            if(rating == "5"):
                texts.append(content[x])
                ratings.append('5')
                types.append(type)
                rated +=1
            #Anti racist remark
            elif(rating == "1"):
                texts.append(content[x])
                ratings.append('1')
                types.append(type)
                rated +=1
            else:
                print("Invalid Entry")
                print(content[x])
                continue
            d = {'text': texts, 'sentiment': ratings, 'types':types}
            df = pd.DataFrame(data=d)
            with open('train.csv', 'a') as f:
                df.to_csv(f, header=False)
            break

label("raw_tweets.txt")
