import requests
from bs4 import BeautifulSoup as bs

link = "https://www.flipkart.com/watches/pr?sid=r18"
url = requests.get(link)
#soup = bs(url.text)
#elements = soup.find_all("div",class_="_1AtVbE col-12-12")

