from osmcheck import api

from .conf import DEFAULT_REGION_KEY


if __name__ == "__main__":
    from pprint import pprint

    entries = api.query_osm(DEFAULT_REGION_KEY)
    for entry in entries[:10]:
        pprint(entry)
        pprint(api.check(entry))
