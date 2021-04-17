import requests

from typing import Optional

from .check import Check, register_check
from .osm import OsmEntry


@register_check
class CheckWebsite(Check):
    """ Some OsmEntries have a website within their tags. This Check tries to
        access this webpage. A non-existing webpage might be a hint.
    """

    @staticmethod
    def eval(entry: OsmEntry) -> Optional[float]:
        if not "website" in entry.tags:
            return None

        try:
            r = requests.get(entry.tags["website"])
            r.raise_for_status()
            return 0.75
        except:
            return 0.25
