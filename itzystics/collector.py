import re
import json
import requests
from dotdict import dotdict as dd
from bs4 import BeautifulSoup
from datetime import date


class Youtube:
    def __init__(self, link: str):
        soup = BeautifulSoup(requests.get(link).text, "html.parser")

        meta = {}
        for e in soup.find_all("meta"):
            keys = list(e.attrs.keys())
            meta[e.attrs[keys[1 - keys.index('content')]]] = e.attrs['content']

        self.title = meta['title']
        self.description = meta['description']
        self.views = int(meta['interactionCount'])

        tmp1 = json.loads(re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1))
        tmp2 = tmp1['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]
        tmp3 = tmp2['videoPrimaryInfoRenderer']['videoActions']['menuRenderer']['topLevelButtons'][0]
        tmp4 = tmp3['segmentedLikeDislikeButtonRenderer']['likeButton']['toggleButtonRenderer']['toggledText'][
            'accessibility']['accessibilityData']['label']
        self.likes = int(re.search(r"[0-9,]+", tmp4).group(0).replace(',', ''))

        self.author = dd()
        self.author.link = \
            [link['href'] for link in soup.find_all('link', itemprop='url') if link['href'].find('@') != -1][0]
        self.author.name = soup.find('link', itemprop='name')['content']

        self.keywords = meta['keywords'].split(', ')
        self.date_published = date.fromisoformat(meta['datePublished'])
        self.date_upload = date.fromisoformat(meta['uploadDate'])

        self.video = dd()
        self.video.link = meta['og:url']
        self.video.size = (meta['width'], meta['height'])

        self.thumbnail = dd()
        self.thumbnail.link = meta['og:image']
        self.thumbnail.size = (meta['og:image:width'], meta['og:image:height'])

    def __repr__(self):
        return f'🎬(🏷️="{self.title}", 👤={self.author.name}, 📆={self.date_upload}, 👁️‍🗨️={self.views}, 👍={self.likes})'

    __str__ = __repr__
