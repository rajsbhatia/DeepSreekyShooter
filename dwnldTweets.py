import twint
from tqdm import tqdm
import csv

# TODO: determine if tweet is a reply
def is_reply(tweet):
	# TODO: remove 
	return


# TODO: show tweets after searching
# TODO: add removal of links, removing hashtags, usertags, links, replies from tweets
def scrapeTweets(username="sreekyshooter", limit=None, includeReplies=False, includeLinks=False, 
	removeUserTags=False, removeHashTags=False):
	config = twint.Config()
	if limit:
		assert limit % 10 == 0, "'limit' must be multiple of 10"
	else: # if no limit given, get limit
		config.Username = "sreekyshooter"
 		# config.Profile_full = True # in case of shadow ban enable this
		config.Store_object = True # store tweets as json objs
		config.Hide_output = True # enable to hide output of running twint search
		# config.Store_csv = True
#		config.Format = "Tweet id: {id} | Date: {date} | Time: {time} | Tweet: {tweet}"
		if includeLinks is True:
			config.Links = "include"
		else:
			config.Links = "exclude"
		
		twint.run.Search(config)
		tweets = twint.output.tweets_list
		limit = len(tweets)
		print(limit)



if __name__ == "__main__":
	scrapeTweets()