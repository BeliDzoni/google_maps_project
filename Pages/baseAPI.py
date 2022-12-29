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