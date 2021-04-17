from here_places_api import here_api_request
from osmcheck.api import OsmEntry, register_check, Check, CheckTimestamp


#@register_check
class HerePlacesCheck(Check):

    @staticmethod
    def eval(entry: OsmEntry):
        # if no name tag exists, this check cant be used
        if not 'name' in entry.tags:
            return None

        items = here_api_request(entry.tags['name'], entry.lat, entry.lon)
        if not 'items' in items:
            print("Error: Answer did not contain a key called 'items'")
            return None

        return (.75 if (len(items['items']) > 0) else .2)


if __name__ == "__main__":
    testEntry = OsmEntry(
        400,
        '50.8097633',
        '8.7722088',
        'test',
        {'name': 'Shawarma Haus'},
    )

    print(HerePlacesCheck.eval(testEntry))
