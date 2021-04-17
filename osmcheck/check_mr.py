from osmcheck import api

from .conf import DEFAULT_REGION


if __name__ == "__main__":
    from pprint import pprint

    entries = api.query_osm(DEFAULT_REGION)
    for entry in entries[:10]:
        pprint(entry)
        pprint(api.check(entry))
