import requests


class API:

    def __init__(self):
        pass

    @staticmethod
    def _request(url):
        try:
            response = requests.head(url)
            return url, response.status_code
        except Exception:  # SSL error, timeout, host is down, firewall block, etc.
            print(url, 'ERROR')
            return url, None

    def _get(self, url, headers=None, payload=None, params=None):
        if headers is None:
            headers = {}
        if payload is None:
            payload = {}
        if params is None:
            params = {}
        try:
            response = requests.get(url, headers=headers, data=payload, params=params)
            return response.json()
        except Exception:
            print(url, 'ERROR')
            return url
