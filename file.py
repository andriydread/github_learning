import requests
import datetime


r = requests.get('https://hacker-news.firebaseio.com/v0/item/123134.json?print=pretty')
print(r.json())
unix_time = r.json()['time']
to_date_time = datetime.datetime.fromtimestamp(unix_time)


print(to_date_time)


x = requests.get('https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty')

print(x.json())


y = requests.get('https://hacker-news.firebaseio.com/v0/beststories.json?print=pretty')

print(y.json())


# New