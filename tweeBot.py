import tweepy
from tweepy import OAuthHandler
from tweepy import API
import twitter_credentials
from twitter_credentials import FILE_NAME
import time

# Authentication Class
class TwitterAuth():
    
    def auth_tokens(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_KEY, twitter_credentials.ACCESS_SECRET)
        return auth

# Instantiate TwitterAuthenticator
twitter_auth = TwitterAuth()

# Instantiate API Object
api = API(twitter_auth.auth_tokens())

def retrieve_last_seen_id(FILE_NAME):
    f_read = open(FILE_NAME, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, FILE_NAME):
    f_write = open(FILE_NAME, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets .... ')
    # DEV NOTE: Use origin ID 1163880599008026625 for testing
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

    for m in reversed(mentions):
        print(str(m.id) + '--' + m.full_text)
        last_seen_id = m.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#oi' in m.full_text.lower():
            print('Found hello world!')
            print('Responding back ... ')
            api.update_status('@' + m.user.screen_name + '#pineapple big massive pineapple ..... sunshine!', m.id)

while True:
    reply_to_tweets()
    time.sleep(2)
