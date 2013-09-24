import sys
import json

words_count = 0.0

new_sentiment_scores = {}

tweet_list = []
tweets_dict_list = []

def init_sentiment_values(sent_file):
    scores = {} # initialize an empty dictionary
    for line in sent_file:
  	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  	scores[term] = int(score)  # Convert the score to an integer.

    return scores

def init_tweet_list(tweet_file):
    json_data = []
    for line in tweet_file:
        json_data.append(json.loads(line))

    text = []
    for tweet in json_data:
	if "place" in tweet:
	    text.append(tweet["place"])

    return text

def sentiment_value(tweet_msg):
    global new_sentiment_scores, words_count
    
    value = 0.0
    words = tweet_msg.split()

    for term in words:
	words_count = words_count + 1.0
	if term in new_sentiment_scores:
	    new_sentiment_scores[term]["count"] = new_sentiment_scores[term]["count"] + 1
	else:
	   dic = {}
	   dic["count"] = 1
	   
	   new_sentiment_scores[term] = dic 
	   

    return value

def tweets_sentiment_value(tweet_file):
    global tweets_dict_list, tweet_list, words_count

    tweet_list = init_tweet_list(tweet_file)
    for tweet_msg in tweet_list:
        sentiment_value(tweet_msg)

    for term in new_sentiment_scores.keys():

	dic = new_sentiment_scores[term]
	dic["frequency"] = dic["count"]/words_count

	print term + " " + str(dic["frequency"])

def main():
    tweet_file = open(sys.argv[1])
    tweets_sentiment_value(tweet_file)
    

if __name__ == '__main__':
    main()
