import requests as r
from bs4 import BeautifulSoup

quote_classes = ["m-h6u0fa","enfjjrk0"]

page = r.get("https://app.mobalytics.gg/ar_ar/lor/cards")

soup = BeautifulSoup(page.text, 'html.parser')

text = soup.get_text("")
print(text)

# for line in page.iter_lines():
#     print(line)

