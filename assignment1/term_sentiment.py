import sys
import json

words_count = 0.0

sentiment_scores = {}
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
	if "text" in tweet:
	    text.append(tweet["text"])

    return text

def sentiment_value(tweet_msg):
    global sentiment_scores, new_sentiment_scores, words_count
    
    value = 0.0
    words = tweet_msg.split()

    new_terms_list = []

    for word in words:
	words_count = words_count + 1.0
	if word in sentiment_scores:
	    value = value + float(sentiment_scores[word])
	else:
	   new_terms_list.append(word)

    for term in new_terms_list:
	if term in new_sentiment_scores:
	    new_sentiment_scores[term]["count"] = new_sentiment_scores[term]["count"] + 1
	    new_sentiment_scores[term]["sentiment_before"] = new_sentiment_scores[term]["sentiment_before"] + value
	else:
	   dic = {}
	   dic["count"] = 1
	   dic["sentiment_before"] = value
	   
	   new_sentiment_scores[term] = dic 
	   

    return value

def tweets_sentiment_value(tweet_file):
    global tweets_dict_list, tweet_list, words_count

    tweet_list = init_tweet_list(tweet_file)
    for tweet_msg in tweet_list:
        dic = {}
	dic["text"] = tweet_msg
        dic["sentiment"] = sentiment_value(tweet_msg)
	tweets_dict_list.append(dic)

    for term in new_sentiment_scores.keys():

	dic = new_sentiment_scores[term]
	dic["sentiment"] = dic["sentiment_before"]/dic["count"] 
	dic["frequency"] = dic["count"]/words_count

	print term + " " + str(dic["sentiment"])

def main():
    global sentiment_scores

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sentiment_scores = init_sentiment_values(sent_file)
    tweets_sentiment_value(tweet_file)
    

if __name__ == '__main__':
    main()
