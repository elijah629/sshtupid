import requests
from bs4 import BeautifulSoup
from pprint import pprint

news = {}

### Get first 5 news items from news.google.com (Switzerland)
url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-CH&gl=CH&ceid=CH%3Aen"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="i10-panel")
results = results.find_all("c-wiz")[0].find_all("c-wiz")
for i in range(0, 10, 2):
    s = "123"
    news[results[i].find_all("h4")[0].text] = results[i].find_all("a")[0]["href"].replace(".", "https://news.google.com", 1)

pprint(news)