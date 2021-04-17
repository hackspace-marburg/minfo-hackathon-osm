import requests
import sys

api_token = sys.argv[1]

print("Here Places api token: {}".format(api_token))
r = requests.get(
    'https://discover.search.hereapi.com/v1/discover',
    params = {
        'at' : '52.5228,13.4124',
        'q' : 'petrol+station',
        'apiKey' : '{}'.format(api_token)
    })

print(r.headers)
print(r.content)
