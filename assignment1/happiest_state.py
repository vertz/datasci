import sys
import json

happy_dict = {}
sentiment_scores = {}

tweet_list = []

def init_sentiment_values(sent_file):
    scores = {} # initialize an empty dictionary
    for line in sent_file:
  	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  	scores[term] = int(score)  # Convert the score to an integer.

    return scores

def sentiment_value(tweet):
    global sentiment_scores
    
    if "text" in tweet:
	tweet_msg = tweet["text"]
    else:
	return 0

    value = 0.0
    words = tweet_msg.split()

    for word in words:
	if word in sentiment_scores:
	    value = value + float(sentiment_scores[word])

    return value

def init_tweets_happy_list(tweet_file):
    global happy_dict

    json_data = []
    for line in tweet_file:
        json_data.append(json.loads(line))

    for tweet in json_data:
	if "place" in tweet:
	    if type(tweet["place"]) == dict:
	    	if "country_code" in tweet["place"]:
		    if tweet["place"]["country_code"] == "US":	
			if "full_name" in tweet["place"]:
				place = tweet["place"]["full_name"]
				place = place[-2:]
				if place in happy_dict:
					value = sentiment_value(tweet)/happy_dict[place]["count"]
					happy_dict[place]["count"] = happy_dict[place]["count"] + 1.0
					happy_dict[place]["value"] = happy_dict[place]["value"] + value
				else:
					happy_dict[place] = {}
					happy_dict[place]["count"] = 1.0
					happy_dict[place]["value"] = sentiment_value(tweet)

    maximum = float("-inf")
    state = ""

    for place in happy_dict.keys():
	if (happy_dict[place]["value"] > maximum):
	   maximum = happy_dict[place]["value"]
	   state   = place

    print place

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sentiment_scores = init_sentiment_values(sent_file)
    init_tweets_happy_list(tweet_file)
    

if __name__ == '__main__':
    main()
