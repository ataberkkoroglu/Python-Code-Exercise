import requests
from bs4 import BeautifulSoup
url="https://teknolojsi.net/"
response=requests.get(url)
Html_içeriği=response.content
soup=BeautifulSoup(Html_içeriği,"html.parser")
print(soup.find_all())