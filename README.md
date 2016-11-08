# README #

Twitter Data Mining project for CSCI 581 Fall 2016.

### What is this repository for? ###

* Online, real-time twitter analysis of sentiment with tweets related to sectarianism.
* Version .001
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###
Mac:

* [Install docker](https://docs.docker.com/engine/installation/)
* [Install Tweepy](http://www.tweepy.org/): pip install Tweepy
* [Install Textblob](https://textblob.readthedocs.io/en/dev/): pip install textblob
* [Install Python Elasticsearch](https://elasticsearch-py.readthedocs.io/en/master/): pip install elesticsearch
* [Pull Docker file from hub](https://hub.docker.com/r/nshou/elasticsearch-kibana/): docker pull nshou/elasticsearch-kibana
* Start: docker run -d -p 9200:9200 -p 5601:5601 nshou/elasticsearch-kibana

Elasticsearch now accessible via [localhost:9200](localhost:9200) and Kibana via [localhost:5601](localhost:5601)
### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact