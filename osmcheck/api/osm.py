import overpass

from functools import lru_cache
from datetime import datetime
from typing import Dict, List, NamedTuple


class OsmEntry(NamedTuple):
    "Representation of a shops entry in OSM."
    osm_id: int
    lat: float
    lon: float
    timestamp: datetime
    tags: Dict[str, str]

    def __repr__(self) -> str:
        if "name" in self.tags:
            return f"OsmEntry({self.osm_id}, {self.tags['name']})"
        return f"OsmEntry({self.osm_id})"

    def __hash__(self) -> int:
        return self.osm_id


@lru_cache(maxsize=128)
def query_osm(region: str) -> List[OsmEntry]:
    "List all shops within the specified region."
    api = overpass.API()
    resp = api.get(
        f"area[name='{region}'];node['shop'](area);",
        verbosity="meta",
        responseformat="json",
    )
    return [
        OsmEntry(
            ele["id"],
            ele["lat"],
            ele["lon"],
            datetime.strptime(ele["timestamp"], "%Y-%m-%dT%H:%M:%SZ"),
            ele["tags"],
        )
        for ele in resp["elements"]
        if ele["type"] == "node"
    ]
