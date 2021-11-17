import pywhatkit
import requests
import time
from my_inputs   import  talk


def bitcoin():
    main_url = "https://newsapi.org/v2/everything?q=bitcoin&apiKey=2f0834cfb909401a9cca0ce40cd389f2"
    open_google_page = requests.get(main_url).json()
    articles = open_google_page["articles"]

    result = []

    for a in articles:
        result.append(a["title"])

    for i in range(10):
        time.sleep(5)
        Headline = i+1, result[i]
        print(Headline)
        talk(Headline)
if __name__==("__main__"):
    bitcoin()
