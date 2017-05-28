from twitter import *

def getLastEPNTweet(AT,AT_S,CON,CON_S):
    t = Twitter(auth=OAuth(AT,AT_S,CON,CON_S))
    tweets = list(t.statuses.user_timeline(screen_name="EPN",count=1))

    #for tweet in tweets:
        #print(tweet['text'])
    return tweets[0]['text'] + " - EPN"
