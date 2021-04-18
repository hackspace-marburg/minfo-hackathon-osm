import requests

from typing import Optional

from .check import Check, register_check
from .osm import OsmEntry

from ..conf import WEB_PORT


@register_check
class CheckJodel(Check):
    """ It is possible to trigger a poll on Jodel from the web UI.
        This is a meme. A working one. It is as good as Mechanical Turk. But free.
    """

    @staticmethod
    def eval(entry: OsmEntry) -> Optional[float]:
        try:
            r = requests.get("http://localhost:{port}/jodel/poll/osm:{osm_id}".format(
                    port=WEB_PORT,
                    osm_id=entry.osm_id
                )
            )
            r.raise_for_status()
            votes = r.json()["poll_votes"]
            yes, no = votes[0], votes[1]
            return yes/(yes+no)
        except:
            return None
