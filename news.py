from bs4 import BeautifulSoup
import requests, random, json, time

newslist = []

# Wikipedia part
req = requests.get("https://en.wikipedia.org/api/rest_v1/page/random/summary")
response = req.json()
print(f"""
Title: {response['title']}
Text: {response['extract']}
URL: {response['content_urls']['desktop']['page']}
""")

# News

url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="i10-panel")
results = results.find_all("c-wiz")[0].find_all("c-wiz")
for i in range(0, len(results), 2):
    print(results[i].find_all("h4")[0].text)

# Random Generator (DO NOT USE)
#newstext = "In this weeks roundup of news!\n\n"
#url = "https://realpython.github.io/fake-jobs/"
#page = requests.get(url)

#soup = BeautifulSoup(page.content, "html.parser")
#for i in range(0, random.randrange(10, 11)):
#    strlength = random.randrange(0, 60)
#    for i in range(0, strlength):
#        newstext += random.choice(open("assets/wordlist/words.txt").readlines()).rstrip('\n')
#        newstext += " "
#    newstext += "\n"

#print(newstext)