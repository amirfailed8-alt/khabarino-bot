import os
import json
import urllib.request
import xml.etree.ElementTree as ET

RSS_SOURCES = [
    "https://www.mehrnews.com/rss",
    "https://www.tasnimnews.com/fa/rss/feed/0/7/0"
]

def get_news():
    for url in RSS_SOURCES:
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": "KhabarinoBot/1.0"}
            )
            with urllib.request.urlopen(req, timeout=15) as r:
                root = ET.fromstring(r.read())

            for item in root.findall(".//item")[:5]:
                title = item.findtext("title", "").strip()
                link = item.findtext("link", "").strip()
                desc = item.findtext("description", "").strip()
                if title and link:
                    yield title, desc, link
        except Exception as e:
            print("خطا در دریافت منبع:", e)

if __name__ == "__main__":
    for title, desc, link in get_news():
        print(title)
        print(desc[:250])
        print(link)
        print("---")