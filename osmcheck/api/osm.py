import overpass

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


def query_osm(south: float, west: float, north: float, east: float) -> List[OsmEntry]:
    "List all shops within the specified bounding box."
    api = overpass.API()
    resp = api.get(
        f"node['shop']({south},{west},{north},{east});",
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
