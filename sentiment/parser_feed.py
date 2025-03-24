#!/usr/bin/env python3

from rss_parser import RSSParser
from requests import get
from bs4 import BeautifulSoup
import translator as tl
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import chardet

ansa = [
    "https://www.ansa.it/sito/notizie/topnews/topnews_rss.xml",
    "https://www.ansa.it/sito/notizie/politica/politica_rss.xml",
    "https://www.ansa.it/sito/notizie/mondo/mondo_rss.xml",
    "https://www.ansa.it/sito/notizie/economia/economia_rss.xml",
    "https://www.ansa.it/sito/notizie/sport/sport_rss.xml",
    "https://www.ansa.it/sito/notizie/sport/calcio/calcio_rss.xml",
    "https://xml2.corriereobjects.it/feed-hp/homepage.xml",
]

analyzer = SentimentIntensityAnalyzer()

# for feed in ansa[5:]:
response = get(ansa[6], timeout=5)
# ... cattura la codifica e impostala
# chardet...
# response.encoding = ...
rss = RSSParser.parse(response.text)


# Iteratively print feed items
for item in rss.channel.items:

    txt = BeautifulSoup(item.title.content, "html.parser")
    print(txt)

    sent = f"{item.title.content}. {item.description.content}"
    print("=" * 100)
    print(sent)
    print("TRANSLATED")
    translated = tl.translate(sent)
    print(translated)
    vs = analyzer.polarity_scores(translated)
    print(vs["compound"])
