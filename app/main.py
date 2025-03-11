from auth import get_twitter_conn
from get_quote import get_quote
import time
import random
import tweepy
from datetime import datetime, timedelta

def main():
    # Connect to Twitter
    client = get_twitter_conn()

    try:
        # Get a random quote
        random_quotes = random.choice(get_quote())

        # Format the quote
        quote = f"'{random_quotes['quote']}' - {random_quotes['author']}"
        
        # Post the tweet
        client.create_tweet(text=quote)
        print("Successful sent tweet")
    
    except tweepy.TweepyException as e:
        # Print error message if tweeting fails
        print(f"Error tweeting {e}")
     
if __name__ == "__main__":
    main()

