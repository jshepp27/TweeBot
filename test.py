import tweepy

FILE_NAME = 'last_seen_id.txt'
CONSUMER_KEY = "ZhSPPDmijJ1xsIrfbRqgE5h05"
CONSUMER_SECRET = "VauRt0VQdxNbKDOdfvX6vtr9fp83xVKAzWs1Nc2Ykodp084TZ1"
ACCESS_KEY = "1156898813598212096-efz1EvT985WY1zPBJwsUdI7FkWwknV"
ACCESS_SECRET = "8mgozFcEeoOBfZDvSE9OJf7eacaFDo4AvXPfIAdA34CPO"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

last_seen_id = retrieve_last_seen_id(FILE_NAME)
mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
                    
for mention in reversed(mentions):
    print(str(mention.id) + ' - ' + mention.full_text)
    last_seen_id = mention.id
    store_last_seen_id(last_seen_id, FILE_NAME)
    if '#helloworld' in mention.full_text.lower():
        print('found #helloworld!')
        print('responding back...')
