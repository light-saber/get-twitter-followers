#Use at your own risk. I am not responsible for any mishaps.
#This requires twitter api
#pip install twitter

#There are times when we need followers from a particular field or those who have similar interests.
#Random following of such twitter handles may or may not help in increasing the number of followers. 
#The problem with following too many people is that your twitter feed will be filled with their tweets, which may not be of interest sometimes. 
#The problem with retweeting is that it will lead to too many tweets from the user and that may not be considered good.
#But when we favourite a tweet, its not made public and slowly but steadily it will help in increasing the followers.
#Since this is a legitimate way of increasing followers, it needs some input from the user too. 
#They must also tweet once in a while on those topics using relevant hashtags. 
#This way you can create a pseudo-conversation where the other person thinks you are reading his tweets but that is never the case.
#This way slowly, but steadily you will increase the number of followers.
#This is know to work best when you use the hashtags pertaining to certain events/conference. 

#Created by light-saber
#Date:2014.06.28


import twitter

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

q = ''
#it should look like this
#q = '#ThisIsTwitter'
count = 
#count = 1000

search_results = twitter_api.search.tweets(q=q, count=count)
statuses = search_results['statuses']

for tweets in statuses:
print tweets['text'], '\n'
result = twitter_api.favorites.create(_id=tweets['id'])
print("favorited: %s" % (result['text'].encode("utf-8")), '\n\n')
