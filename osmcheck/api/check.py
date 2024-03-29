import statistics

from functools import lru_cache
from typing import Dict, Optional, Type

from .osm import OsmEntry


class Check:
    "Abstract base class for checks on OSM entries."

    @staticmethod
    def eval(entry: OsmEntry) -> Optional[float]:
        """ Evaluate this OsmEntry and return the calculated probability.

            The resulting probability must be within [0,1]. A zero value means
            that for this check, this entry cannot exist anymore. However, a one
            means that this entry must exist. If this Check cannot perform an
            evaluation, None must be returned. Of course, every value within the
            interval is possible and an implementation matter.
        """
        raise NotImplementedError("eval was not overridden")


check_types = {}


def register_check(clz: Type[Check]):
    "Register this Check class to be automatically be used."
    check_types[clz.__name__] = clz


@lru_cache(maxsize=1024)
def check(entry: OsmEntry) -> Dict[str, float]:
    "Check an entry against all known Checks."
    return {name[5:]: ct.eval(entry) for name, ct in check_types.items()}


def calc_score(checks: Dict[str, float]) -> float:
    "Calculate a final score based on all Checks."
    checks = [v for k, v in checks.items() if v is not None]
    return statistics.median_high(checks)
