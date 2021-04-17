from .check import Check, register_check
from .osm import OsmEntry


@register_check
class CheckOsmClosed(Check):
    "OSM has some tags to identify closed shops. Let's check them."

    @staticmethod
    def eval(entry: OsmEntry) -> Optional[float]:
        tags = [
            ("disused", "yes"),
            ("shop", "vacant"),
            "disused:shop",
        ]

        for tag in tags:
            if type(tag) is tuple:
                k, v = tag
                if entry.tags.get(k, None) == v:
                    return 0.0
            elif type(tag) is str:
                if tag in entry.tags:
                    return 0.0

        return None
