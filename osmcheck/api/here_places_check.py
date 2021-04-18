import json
import os

import requests

from osmcheck.api import OsmEntry, register_check, Check


def here_api_request(name, latitude, longitude) -> dict:
    with open("here_places_api_key", "r") as keyfile:
        api_token = keyfile.read()
        keyfile.close()

    request_params = {
        'in': 'circle:{},{};r=100'.format(latitude, longitude),
        'q': name,
        'apiKey': '{}'.format(api_token)
    }

    r = requests.get(
        'https://discover.search.hereapi.com/v1/discover',
        params=request_params
    )
    if (r.status_code == 401):
        raise Exception("Bad Here Places api Key")
    r.raise_for_status()

    result = json.loads(r.text)
    return result


@register_check
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
