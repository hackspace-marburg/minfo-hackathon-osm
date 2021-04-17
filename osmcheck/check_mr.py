from osmcheck import api


if __name__ == "__main__":
    from pprint import pprint

    entries = api.query_osm(50.7788, 8.7510, 50.8083, 8.8122)
    for entry in entries[:10]:
        pprint(entry)
        pprint(api.check(entry))
