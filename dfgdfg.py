import requests
from bs4 import BeautifulSoup
import random
user_agent_list = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',

]

user_agent = random.choice(user_agent_list)
headers = {'User-Agent': user_agent}
url = 'https://wr.lordfilm7.link/film2/mjuzikly-filmy/'
page = BeautifulSoup(requests.get(url, headers=headers).text, "lxml")

for name in page.find_all("div", class_="th-item"):
    name_text = name.text
    print(name_text)
for film in page.find_all("div", class_="th-item"):
    Link_STR = film.find("a", class_="th-in with-mask").get('href')
    print(Link_STR)

