import sys
import json

words_count = 0.0

hashtags_dict = {}

tweet_list = []

def init_tweets_hashtags_list(tweet_file):
    global hashtags_dict

    json_data = []
    for line in tweet_file:
        json_data.append(json.loads(line))

    for tweet in json_data:
	if "entities" in tweet:
	    if "hashtags" in tweet["entities"]:
		for tag in tweet["entities"]["hashtags"]:
		    if "text" in tag:
	                if tag["text"] in hashtags_dict:
			    hashtags_dict[tag["text"]] = hashtags_dict[tag["text"]] + 1.0
		        else:
			    hashtags_dict[tag["text"]] = 1.0

    hashtags_dict_list = []
    for tag in hashtags_dict.keys():
	dic = {}
	dic["count"] = hashtags_dict[tag]
	dic["text"] = tag
	hashtags_dict_list.append(dic) 

    from operator import itemgetter
    newlist = sorted(hashtags_dict_list, key=itemgetter("count")) 
    newlist.reverse()

    for i in range(10):
	print newlist[i]["text"] + " " + str(newlist[i]["count"])

def main():
    tweet_file = open(sys.argv[1])
    init_tweets_hashtags_list(tweet_file)
    

if __name__ == '__main__':
    main()
