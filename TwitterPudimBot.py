import tweepy
import time
from datetime import datetime as dt

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
tweets_to_retweet = []
tweets_total = []

while(True):    
    tweets = tweepy.Cursor(api.search,count="10", q="pudim", since="2019-01-11").items()
    for tweet in tweets:
        try:            
            tweet_id = tweet._json['id']
            isValid = True
            #verifica se a palavra não é o noma do usuário ou reply para meu usuário
            if ('pudim' in tweet._json['user']['name'] or 'GostosoPudim' in tweet._json['user']['name'] ):
                isValid = False
            if ('pudim' in tweet._json['user']['screen_name'] or 'Oi, eu sou um pudim' in tweet._json['user']['screen_name'] ):
                isValid = False
            #armazena tweets
            if (tweet_id not in tweets_to_retweet and isValid):
                tweets_to_retweet.append(tweet_id)
            if (tweet_id not in tweets_total and isValid):
                tweets_total.append(tweet_id)
            if(len(tweets_to_retweet)> 0):
                next_id = tweets_to_retweet[0]
                del tweets_to_retweet[0]
                api.retweet(next_id)
                print("Retweet... ")            
        except tweepy.TweepError as error:
            print("Erro.. ", error, " ", dt.now().time())
        time.sleep(40)