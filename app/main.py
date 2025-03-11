from auth import get_twitter_conn
from get_quote import get_quote
import time
import random
import tweepy



def main():
   # Connect to Twitter
    client = get_twitter_conn()

    try:
        random_quotes = random.choice(get_quote())

        quote = f"'{random_quotes['quote']}' - {random_quotes['author']}"
        client.create_tweet(text=quote)
        print("Successful sent tweet")
    
    except tweepy.TweepyException as e:
        print(f"Error tweeting {e}")
     
if __name__ == "__main__":
    main()

