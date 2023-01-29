import codetiming
import httpx
from selectolax.parser import HTMLParser

t = codetiming.Timer(name="execTime")
t.start()

for page in range (1,51):
    print(f"page {page}")
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    req = httpx.get(url,timeout=None)
    html = HTMLParser(req.text)
    selector = ".product_pod a[title]"
    tags = html.css(selector)

    for tag in tags:
        print(tag.text())

t.stop()