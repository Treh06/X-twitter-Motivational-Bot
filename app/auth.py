import tweepy
from keys import API_key, API_key_secert, access_token, access_secert


def get_twitter_conn():
    try:
         # Create the OAuth1Handler for Twitter API
        client = tweepy.Client(
            consumer_key=API_key, 
            consumer_secret=API_key_secert,
            access_token=access_token, 
            access_token_secret=access_secert
        )
        return client

    # Verification fails
    except tweepy.TweepyException as e:
        print("Error Authenticating", e)
        return None