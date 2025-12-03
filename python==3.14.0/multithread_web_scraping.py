import threading
import requests
from bs4 import BeautifulSoup #Beautiful soup 4


#The Urls that will be getting webscraped
url1 = "https://roadoftheking.com/ocg-2025-10-metagame-report-6-7/"
url2 = "https://www.yugiohmeta.com/top-decks"
url3 = "https://docs.langchain.com/oss/python/integrations/providers/searchapi"

urls = [
    url1,
    url2,
    url3
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    print(f"The content: /n {soup.text}")

threads = []

for url in urls:
    thread = threading.Thread(target = fetch_content, args = (url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched!")