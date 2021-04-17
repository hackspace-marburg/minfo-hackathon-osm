import requests
import sys
import json
from pprint import pprint

api_token = sys.argv[1]


def here_api_request(name, latitude, longitude) -> dict:
    request_params = {
            'in': 'circle:{},{};r=100'.format(latitude, longitude),
            'q': name,
            'apiKey' : '{}'.format(api_token)
        }
    print("Here Places Api: using the following Parameters for the Entrypoint 'Discover':")
    print(request_params)

    r = requests.get(
        'https://discover.search.hereapi.com/v1/discover',
        params = request_params
    )
    if(r.status_code == 401):
        raise Exception("Bad Here Places api Key")
    print(r.text)
    r.raise_for_status()

    print("Received Data:")
    print(r.headers)
    print("Status Code: {}".format(r.status_code))
    result = json.loads(r.text)
    pprint(result)
    return result