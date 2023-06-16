import requests
import time
from bs4 import BeautifulSoup

url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-US&gl=US&ceid=US%3Aen"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="i10-panel")
results = results.find_all("c-wiz")[0].find_all("c-wiz")
for i in range(0, len(results), 2):
    print(results[i].find_all("h4")[0].text)