import json
import requests
import warnings


def parse_url(url):
    raw_response = _get_url(url)
    return _parse_json_response(raw_response)


def _get_url(url):
    return requests.get(url)


def _parse_json_response(r):
    if r.status_code == 200:
        return json.loads(r.content.decode('utf-8'))
    else:
        warnings.warn(f"Request returned: {r.status_code}")
        return None