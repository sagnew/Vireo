import urllib
import simplejson
import random

def searchTweets(query):
    search = urllib.urlopen("http://search.twitter.com/search.json?q=lang%3Aen%20"+query)
    dict = simplejson.loads(search.read())
    return random.choice(dict["results"])["text"]
