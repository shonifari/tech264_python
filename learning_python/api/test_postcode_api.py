import requests
from pprint import pprint

post_codes_req = requests.get("https://api.postcodes.io/postcodes/sw162xn")


# print(f"Status code: {post_codes_req.status_code}")
# print(f"Headers: {post_codes_req.headers}")
# print(f"Content: {post_codes_req.content}")
#
# pprint(f"Data type of JSON: {type(post_codes_req.json_folder())}")
# pprint(post_codes_req.json_folder())


# POST REQ

import requests
import json

json_body = json.dumps({'postcodes': ["PR3 0SG", "M45 6GN", "EX165BL"]})

headers = {'Content-Type': 'application/json_folder'}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

pprint(post_multi_req.json())