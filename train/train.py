import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords


def train(data, targets, k=5):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(data, targets)
    return knn


def check_model(model, test_data, targets):
    total = correct = 0
    predictions = model.predict(test_data)
    for i, prediction in enumerate(predictions):
        total += 1
        if prediction == targets[i]:
            correct += 1

    return correct/total


if __name__ == '__main__':
    data = pd.read_csv('train.csv')
    sentiments = data.ix[:, 1]
    categories = data.ix[:, 3]
    text = data.ix[:, 2]
    stop_words = stopwords.words('english')
    tknzr = TweetTokenizer()

    word_list = set()
    tweets = []
    for tweet in text:
        tokenized = [word for word in tknzr.tokenize(tweet.lower())
                     if word not in stop_words]
        tweets.append(tokenized)
        word_list.update(tokenized)

    vectors = []
    for tweet in tweets:
        vectors.append([1 if word in tweet else 0 for word in word_list])

    sent_model = train(vectors, sentiments, k=2)
    cat_model = train(vectors, categories, k=2)

    sent = check_model(sent_model, vectors, sentiments)
    print('Correct: {}%'.format(100*sent))
    cat = check_model(cat_model, vectors, categories)
    print('Correct: {}%'.format(100*cat))
