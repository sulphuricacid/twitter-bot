import tweepy as tp
import time
import os

# credentials to login to twitter api
consumer_key = '*****************Rq9HsU'
consumer_secret = '********************2P7o0pKAQxtt'
access_token = '*********************nRXEY7UhgyhoEWQJDA'
access_secret = '*************************X5rTaQHs9Ab'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('models')

# iterates over pictures in models folder
for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    time.sleep(3)
