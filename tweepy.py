from urllib import response
import config
import tweepy

client = tweepy.Client(bearer_token=config.ACADEMIC_BEARER_TOKEN)

query = 'tokyo 2020 summer olympics -is:retweet'

start_time = '2021-05-01T00:00:00Z'

end_time = '2021-09-01T00:00:00Z'

file_name = datas.txt

response = client.search_all_tweets(query=query, max_results=10000, start_time=start_time, end_time=end_time)

with open(file_name, 'a+') as filehandler:
    for tweet in tweepy.Paginator(client.search_all_tweets, query=query, max_results=10000, start_time=start_time, end_time=end_time)
         filehandler.write('%s\n' % tweet.text)
