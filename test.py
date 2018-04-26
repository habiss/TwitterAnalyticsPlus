from __future__ import absolute_import, print_function

import tweepy
import simple_content

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

print("Hello")

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key = 'HbZtZIbWlAlDmrDyKgcssTBZY'
consumer_secret = 'VQr0r3LaETOmJWJ4VZxco7lwWIq2RuXy4uLXD0WRHdAWaXbwSH'

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token = '983388258288599040-kxqW9IFDEclkqTMh5CNXduOGBEU5AU2'
access_token_secret = 'HKIkCdrAaJ6cMxEmqIEvBgWdwDecEq7Uv97E6dpAbiRTl'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# I/O Placeholder
print("This tool will help you analyze a public account on twitter based on the accounts they follow.")
name = input('Username on Twitter(public accounts only): ')

print("First, let's get a list of the most recent tweets from the people you follow.")

user = api.get_user(name)

print ()
print ("****** Testing the twitter anaylytics platform ********")
print ()

# Initialize a list here

# Define a function to parse all the information from the list

# A dictionary for each user's screen name and their tweets
user_tweets = {}

for friend in user.friends(count=10):
    # print ("Follower: " + friend.screen_name + "\n")
    # print (friend.screen_name)
    search = friend.screen_name
    try:
        all_tweets = ""
        tweets = api.user_timeline(
            screen_name=search, count=1, tweet_mode="extended")
        for tweet in tweets:
            all_tweets += tweet.full_text
        print (search)
        try:
            print ("Here is the classification")
            simple_content.classify(all_tweets)
            simple_content.simple_classify(all_tweets)
        except:
            print ("Error. The user likely has protected tweets")

        # Create dictionary with everything
        user_tweets[search] = all_tweets

    except tweepy.TweepError:
        print ("This user has protected tweets. Failed to run")


simple_content.print_categories()
