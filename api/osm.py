import overpass

from typing import Dict, List, NamedTuple, Tuple


class OsmEntry(NamedTuple):
    "Representation of shops resp. point entries in the OSM."
    osm_id: int
    location: Tuple[float]
    properties: Dict[str, str]

    def __repr__(self) -> str:
        if "name" in self.properties:
            return f"OsmEntry({self.osm_id}, {self.properties['name']})"
        return f"OsmEntry({self.osm_id})"


def query_osm(south: float, west: float, north: float, east: float) -> List[OsmEntry]:
    "List all shops within the specified bounding box."
    api = overpass.API()
    resp = api.get(f"node['shop']({south},{west},{north},{east});")
    return [
        OsmEntry(f.id, f.geometry.coordinates, f.properties)
        for f in resp.features
        if f.geometry.type == "Point"
    ]


if __name__ == "__main__":
    from pprint import pprint

    pprint(query_osm(50.7788, 8.7510, 50.8083, 8.8122))
