# README #

Twitter Data Mining project for CSCI 581 Fall 2016.

### What is this repository for? ###

* Online, real-time twitter analysis of sentiment with tweets related to sectarianism.
* Version .001
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)
* Currently, creates a twitter stream listener (from tweepy), gets the info we want, adds it to elasticsearch.  In the future, can view data with Kibana in various ways based on the data pulled into elasticsearchDB.

### How do I get set up? ###
Mac:

* [Install docker](https://docs.docker.com/engine/installation/)
* [Install Tweepy](http://www.tweepy.org/): pip install Tweepy
* [Install Textblob](https://textblob.readthedocs.io/en/dev/): pip install textblob
* [Install Python Elasticsearch](https://elasticsearch-py.readthedocs.io/en/master/): pip install elesticsearch
* [Pull Docker file from hub](https://hub.docker.com/r/nshou/elasticsearch-kibana/): docker pull nshou/elasticsearch-kibana
* Start: docker run -d -p 9200:9200 -p 5601:5601 nshou/elasticsearch-kibana

Elasticsearch now accessible via [localhost:9200](localhost:9200) and Kibana via [localhost:5601](localhost:5601)

When browsing to kibana, uncheck the selected box, and put the index as sentiment*

[Getting started with Kibana](https://www.elastic.co/guide/en/kibana/current/introduction.html): https://www.elastic.co/guide/en/kibana/current/introduction.html

[Getting started with Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html

A useful command:

    curl -XDELETE 'localhost:9200/sentiment'

Deletes the index sentiment and all its tweets.  Do this if you are updating what sent.py stores in ElasticSearch.

### Some things to look out for: ###

*If you are getting "401" errors, try resetting your system clock.  Twitter streams will return unauthorized if the time of your system is 
### Contribution guidelines ###

* Not yet written

### Who do I talk to? ###

* Morgan Dock