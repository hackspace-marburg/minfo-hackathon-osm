import datetime

from typing import Optional

from .check import Check, register_check
from .osm import OsmEntry


@register_check
class CheckTimestamp(Check):
    """ Each OsmEntry has a timestamp field representing the last changeset
        related to this entry. Thus, one can extrapolate that a very old entry
        which was not touched quite a while might be outdated.
    """

    @staticmethod
    def eval(entry: OsmEntry) -> Optional[float]:
        delta = datetime.datetime.now() - entry.timestamp
        months = int(delta.days / 30.0)

        return max(1.0 - (months / 100.0), 0.0)
