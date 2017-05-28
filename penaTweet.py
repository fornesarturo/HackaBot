import random
from twitter import *

def getLastEPNTweet(AT,AT_S,CON,CON_S):
    t = Twitter(auth=OAuth(AT,AT_S,CON,CON_S))
    tweets = list(t.statuses.user_timeline(screen_name="EPN",count=100))
    return random.choice(tweets)['text'] + " - EPN"
