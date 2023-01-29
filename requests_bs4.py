import codetiming
import requests
from bs4 import BeautifulSoup

t = codetiming.Timer(name="execTime")
t.start()

for page in range (1,51):
    print(f"page {page}")
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    req = requests.get(url)
    html = BeautifulSoup(req.text,"html.parser")
    selector = "h3"
    tags = html.find_all(selector)

    for tag in tags:
        print(tag.text)

t.stop()