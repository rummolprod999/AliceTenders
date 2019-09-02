import json

import requests


def get_tenders_from_server(query):
    r = requests.post("http://86.57.133.250:6342/get_tenders.php", data={'req': query})
    return json.loads(r.text)
