## Tweet Sectarian Analysis Project
This is a project that was done to score the sentiment on topics of common forms of descrimination. 

### What is this repository for? ###

* Online, real-time twitter analysis of sentiment with tweets related to sectarianism.
* Version .1
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Install requirements.txt with pip
* setup `config.py`
* make sure there is labeled, trainable data at labels/train.csv
* run `sent.py` 
* Browse to 5000 port of the machine it is set up on
* /city_statistics/<city_name>/<k> to view top k neg/pos people in a city
* /state_statistics/<state_two_char_iso_code>/<k> to view top k neg/pos people in state
* /statistics/<k> general information charts
* / for Map of tweets

### Some things to look out for: ###

* I actually don't have the final version of the repo because the correct up-to-date csv files are not in this right now, and the existing ones are seriously majorly flawed (no for real, go look at them).  

Guess it never got committed and the machine I originally wrote this on is lost.  

### Contribution guidelines ###

* Submit a PR to merge into master

### Things that can be improved
Pretty much everything.  This was a very introducting project on using Machine Learning on streamed data.

Want to improve it?

- Better / More keywords
- More training data
- Sep classifier for both category and sentiment
- Better classifiers.
- Use a better way to store results from data stream.
