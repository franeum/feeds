#!/usr/bin/env python3

from rss_parser import RSSParser
from requests import get
from bs4 import BeautifulSoup
import translator as tl
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import chardet
import db
import time

start = time.time()
db.init()

ansa = [
    "https://www.ansa.it/sito/notizie/politica/politica_rss.xml",
    "https://www.ansa.it/sito/notizie/mondo/mondo_rss.xml",
    "https://www.ansa.it/sito/notizie/economia/economia_rss.xml",
    "https://www.adnkronos.com/RSS_Ultimora.xml",
    "https://cms.ilmanifesto.it/feed",
    "https://www.internazionale.it/sitemaps/rss.xml",
    "https://www.repubblica.it/rss/esteri/rss2.0.xml",
    "https://www.repubblica.it/rss/politica/rss2.0.xml",
    "https://www.repubblica.it/rss/economia/rss2.0.xml",
    "https://www.linkiesta.it/feed/",
    "http://feed.lastampa.it/Homepage.rss"
]

analyzer = SentimentIntensityAnalyzer()

for feed in ansa:
    response = get(feed, timeout=5)
    response.encoding = chardet.detect(response.content)['encoding']
    rss = RSSParser.parse(response.text)

    for item in rss.channel.items:
        try:
            _title = BeautifulSoup(item.title.content, "html.parser")
            _description = BeautifulSoup(
                item.description.content, "html.parser")

            titleDescription = f"{_title.getText().strip(None)}. {_description.getText().strip(None)}"
            print(titleDescription)
            date = item.content.pub_date.content
            print(date)
            print()
            print("TRANSLATED")
            print()
            translated = tl.translate(titleDescription)
            print(translated)
            print()
            vs = analyzer.polarity_scores(translated)
            compound = vs["compound"]
            print(compound)
            print('*' * 50)

            print("INSERT INTO DB")
            db.insert_value(titleDescription, translated, compound, date)

        except Exception as e:
            print(f"ERRORE GLOBALE: {e}")
            continue

db.commit()
db.close()
print(f"DONE IN {time.time() - start} seconds")
