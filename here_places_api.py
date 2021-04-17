import requests
import sys
import json
from pprint import pprint

api_token = sys.argv[1]


def here_api_request(name, latitude, longitude) -> dict:
    print("Here Places api token: {}".format(api_token))
    request_params = {
            'at' : '{},{}'.format(latitude, longitude),
            'q' : name,
            'apiKey' : '{}'.format(api_token)
        }
    r = requests.get(
        'https://discover.search.hereapi.com/v1/discover',
        params = request_params
    )

    if(r.status_code == 401):
        raise Exception("Bad Here Places Api Key")
    r.raise_for_status()
    print(r.headers)
    print(r.status_code)
    print(r.text)
    result = json.loads(r.text)
    pprint(result)

here_api_request('döner', 50.8161222, 8.7784447)