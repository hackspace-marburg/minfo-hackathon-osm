import bs4
import requests

from typing import Optional

from .check import Check, register_check
from .osm import OsmEntry


@register_check
class CheckGelbeSeiten(Check):
    # TODO

    @staticmethod
    def eval(entry: OsmEntry) -> Optional[float]:
        if not "name" in entry.tags:
            return None
        if not "addr:city" in entry.tags:
            return None

        city, name = entry.tags["addr:city"], entry.tags["name"]

        try:
            r = requests.get(f"https://www.gelbeseiten.de/Suche/{name}/{city}")
            r.raise_for_status()

            soup = bs4.BeautifulSoup(r.text, "html.parser")
            if name.lower() in soup.article.text.lower():
                return 0.75
            return 0.25
        except:
            return None
