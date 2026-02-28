import requests
import time

to_visit = ["https://news.ycombinator.com"]
visited = {"https://news.ycombinator.com":True}

# print(requests.get("https://trufflesecurity.com/blog/google-api-keys-werent-secrets-but-then-gemini-changed-the-rules").content.decode('utf-8'))
nl = 2

start = time.time()

for i in range(120):
	url = to_visit[0]
	nl -=1
	print(i+1,len(to_visit),nl,url)

	response = requests.get(url)
	if response.headers['Content-Type'] == "text/html; charset=utf-8":
		data = response.content.decode('utf-8')
	elif response.headers['Content-Type'] == "text/html":
		data = response.content.decode('utf-8')
	else:
		visited[url] = True
		to_visit = to_visit[1:]
		continue

	separated = data.split('href="')[1:]
	# nl = 0
	for part in separated:
		link = part.split('"')[0]
		if "http" in link:
			nl += 1
			if link not in visited:
				to_visit.append(link)
	visited[url] = True
	to_visit = to_visit[1:]

end = time.time()
print(end-start)




