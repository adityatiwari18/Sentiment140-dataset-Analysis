import re

class Filter:
    tweet=''
    def FilterUsernamesAndURLs():
        global tweet
        tweet = tweet.lower()
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',tweet)
        tweet = re.sub('@[^\s]+','',tweet)
        tweet = re.sub('[\s]+', ' ', tweet)
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
        tweet = tweet.strip('\'"')
        return tweet
