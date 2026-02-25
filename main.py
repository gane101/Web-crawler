
import requests
import time

to_visit = ["https://news.ycombinator.com"]
visited = {"https://news.ycombinator.com":True}

start = time.time()

for i in range(10):
	url = to_visit[0]
	print(url)

	response = requests.get(url)
	data = response.content.decode('utf-8')
	separated = data.split('href="')[1:]

	for part in separated:
		link = part.split('"')[0]
		if "http" in link and link not in visited:
			to_visit.append(link)
			# print(link)
	visited[url] = True
	to_visit = to_visit[1:]

end = time.time()
print(end-start)




