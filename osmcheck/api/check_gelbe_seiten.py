import bs4
import requests

from typing import Optional

from .check import Check, register_check
from .osm import OsmEntry

from ..conf import DEFAULT_CITY


@register_check
class CheckGelbeSeiten(Check):
    "Check an OsmEntry against the Gelbe Seiten (yellow pages)."

    @staticmethod
    def eval(entry: OsmEntry) -> Optional[float]:
        if not "name" in entry.tags:
            return None

        name = entry.tags["name"]
        city = entry.tags["addr:city"] if "addr:city" in entry.tags else DEFAULT_CITY

        try:
            r = requests.get(f"https://www.gelbeseiten.de/Suche/{name}/{city}")
            r.raise_for_status()

            soup = bs4.BeautifulSoup(r.text, "html.parser")
            if name.lower() in soup.article.text.lower():
                return 0.75
            return 0.25
        except:
            return None
