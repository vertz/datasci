import sys
import json

sentiment_scores = {}

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

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
    global sentiment_scores
    
    value = 0.0
    words = tweet_msg.split()

    for word in words:
	if word in sentiment_scores:
	    value = value + float(sentiment_scores[word])

    print value

    return value

def main():
    global sentiment_scores

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sentiment_scores = init_sentiment_values(sent_file)

    tweet_list = init_tweet_list(tweet_file)
    for tweet_msg in tweet_list:
	sentiment_value(tweet_msg)

if __name__ == '__main__':
    main()
