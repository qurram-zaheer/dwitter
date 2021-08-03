import os
from time import time
import tweepy
from dotenv import load_dotenv
from helpers import Configuration, bcolors
import datetime

load_dotenv()
clear = lambda:os.system('clear')

config = Configuration(os.getenv('API_KEY'),os.getenv('API_SECRET_KEY'),os.getenv('BEARER_TOKEN'),os.getenv('ACCESS_TOKEN'),os.getenv('ACCESS_TOKEN_SECRET'))

auth = auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET_KEY)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api=tweepy.API(auth)

follow_list = ['StockDweebs', 'ripster47', 'LuisFinn3']

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        timestamp = datetime.datetime.now()
        uname = status.user.screen_name
        if uname in follow_list:
            if uname == 'StockDweebs':
                uname_color=bcolors.OKBLUE
            elif uname == 'ripster47':
                uname_color=bcolors.OKGREEN
            else:
                uname_color=bcolors.OKGREEN

            print(f"\n{uname_color}{bcolors.BOLD}@" + status.user.screen_name + f"{bcolors.ENDC}\t\t\t\t\t\t\t\t\t\t\t\t"+"["+timestamp.strftime("%H:%M:%S")+"]")
            if hasattr(status, 'extended_tweet'):
                text=status.extended_tweet['full_text']
            else:
                text = status.text
            for word in text.split():
                if word == '#addalert':
                    print(f"{bcolors.BOLD}{bcolors.OKGREEN}" + word, end=' ')
                elif word == '#chartidea':
                    print(f"{bcolors.BOLD}{bcolors.WARNING}" + word, end=' ')
                elif word.startswith("$"):
                    print(f"{bcolors.BOLD}{bcolors.OKCYAN}" + word + f"{bcolors.ENDC}", end=' ')
                else:
                    print(f"{bcolors.HEADER}{bcolors.BOLD}" + word + f"{bcolors.ENDC}",end=' ')
                
            
            
            print(f'{bcolors.OKCYAN}\nhttps://twitter.com/twitter/statuses/' + str(status.id) + f"{bcolors.ENDC}")
            print("######")

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

        # returning non-False reconnects the stream, with backoff.

clear()
stream_listener = MyStreamListener()
stream = tweepy.Stream(auth = api.auth, listener=stream_listener, tweet_mode='extended')

stream.filter(follow=['1260551652479647745', '1054561163843751936', '1355001978200354820'])

